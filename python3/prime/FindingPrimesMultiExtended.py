import multiprocessing as mp
import time

# FindingPrimes benchmark (https://youtu.be/hGyJTcdfR1E)
# 
# This was done based on the code at:
# https://www.the-diy-life.com/can-my-water-cooled-raspberry-pi-cluster-beat-my-macbook/#multi_test_script
#
# There are however a few differences:
# - The provided code was using only one core, I think the pool was not being initialized,
#   this was solved by using python with keyword to enter an executing context with the pool initialized.
#       See also: https://www.python.org/dev/peps/pep-0343/
# - The code provided (and I suspect that the MPI implementation suffers from the same problem), often leaves
#   processing nodes/cores starving for work. I've added a work distribution heuristic that spreads the load better.
# - For ease the comparison and assert the behaviour as the work size increases, I've added a cycle to processes
#   different work sizes in a single script execution.
#
# For reference this is the summary of the execution in an old Intel® Core™ i5-4570 CPU @ 3.20GHz × 4,
#  with Python 3.8.5 in Ubuntu 20.04.2 LTS:
#
#| Method    | Work size | Tasks | Time (s) | Primes | Tasks diff   |
#| basic     | 10000     |     4 |      0.2 |   1229 |      2023124 |
#| halved    | 10000     |     8 |     0.17 |   1229 |      1180260 |
#| heuristic | 10000     |     4 |     0.13 |   1229 |       489729 |
#| basic     | 100000    |     4 |     16.0 |   9592 |    160037669 |
#| halved    | 100000    |     8 |    12.83 |   9592 |     94462972 |
#| heuristic | 100000    |     4 |    10.49 |   9592 |     38916142 |
#| basic     | 200000    |     4 |    63.79 |  17984 |    602879365 |
#| halved    | 200000    |     8 |    49.66 |  17984 |    355443828 |
#| heuristic | 200000    |     4 |    39.26 |  17984 |    146707554 |
#| basic     | 500000    |     4 |   365.16 |  41538 |   3519002684 |
#| halved    | 500000    |     8 |   303.74 |  41538 |   2057500879 |
#| heuristic | 500000    |     4 |   226.27 |  41538 |    851104218 |


# Work sizes to run and compare - Unless you have time to spare, you might want to remove some entries from here...
max_number = [10000, 100000, 200000, 500000]
# One processes per core (this will count the number of online virtual cores using sysconf _SC_NPROCESSORS_ONLN)
num_processes = mp.cpu_count()

def taskDistribution(seq, chunks):
    """
    Naive task distribution of the workload,
    Will simply create ranges segmented linearly
    """
    size = len(seq)
    start = 0
    for i in range(1, chunks + 1):
        stop = i * size // chunks
        yield seq[start:stop]
        start = stop

def bottomTopTaskDistribution(s, e, jobs):
    """
    Task Distribution of the work with a bottom-top heuristic
    
    Distributes the workload by defining 2 ranges for each execution node,
    the bottom numbers and the top numbers ranges, this follows the intuition that
    bigger numbers are harder to compute, so by pairing the biggest with the smallest
    it should help balancing out.
    
    Why is such distribution needed? Because otherwise one of the execution nodes might starve
    for work, while other might be burden with a lot of work.
    
    Note: this distribution might not be the best, but for from my testing it should help a bit
    to fully utilize the available execution nodes for this simple prime computation.
    """
    scopeSize = (e-s+1)/(jobs*2)
    
    startBoundary = s
    endBoundary   = e
    firstResidual = 0
    lastResidual  = 0

    tasks = []
    for t in range(0,jobs):
        first = int(round(startBoundary + scopeSize + firstResidual))
        firstResidual = startBoundary + scopeSize + firstResidual - first
        
        last  = int(round(endBoundary - scopeSize - lastResidual))
        lastResidual = last - (endBoundary - scopeSize - lastResidual)
        
        tasks.append([(startBoundary, first, 1),
                      (last, endBoundary, 1)])
    
        startBoundary = first
        endBoundary = last

    return tasks
    
def batchTasks(tasks):
    """
    Run the primes calculations for each range defined in a list of tuples.
    
    The tuples in the list are the arguments used to define a range.
    
    Returns a tuple with:
       List of primes
       Number of comparisons required
    """
    result = []
    comparisons = 0
    for task in tasks:
        (primes, comparisons) = calc_primes(range(*task))
        result.extend(primes)
    return (result, comparisons)

def calc_primes(numbers):
    """
    Naive computation of prime numbers:
    Compares numbers from an iterable with all the numbers lower than it
    
    Returns tuple with:
       List of primes
       Number of comparisons required    
    """
    num_primes = 0
    primes = []

    comparisons = 0

    #Loop through each number, then through the factors to identify prime numbers
    for candidate_number in numbers:
        found_prime = True
        for div_number in range(2, candidate_number):
            comparisons += 1
            if candidate_number % div_number == 0:
                found_prime = False
                break
        if found_prime:
            primes.append(candidate_number)
            num_primes += 1
    return  primes, comparisons

def main():
    
    def runNaively(pool, nbr, num_tasks):
        #0 and 1 are not primes
        parts = taskDistribution(range(2, nbr, 1), num_tasks)
        #run the calculation
        return pool.map(calc_primes, parts)
    
    def runWithHeuristic(pool, nbr, num_tasks):
        parts = bottomTopTaskDistribution(2, nbr, num_tasks)
        return pool.map(batchTasks, parts)

    def benchmark(pool, nbr, num_tasks, method):
        """
        Benchmarks the performance of a given method.
        Inputs:
            pool         multiprocess Pool
            nbr          Work size (how many numbers will we analyze)
            num_tasks    In how many sub-tasks is the work divided
            method       reference for the method to be benchmarked - signature tuple of method (pool, nbr, num_tasks)
            
        Returns tuple with the following elements:
                Work size, number of sub tasks, time taken, number of primes, sub-tasks work difference
        """
        #Record the test start time
        start = time.time()
        
        results = method(pool, nbr, num_tasks)
          
        # workload optimized task execution:

        primes, comparisons = list(zip(*results))

        total_primes = sum([len(primes_task) for primes_task in primes])
        
        #Once all numbers have been searched, stop the timer
        end = round(time.time() - start, 2)
        
        #Display the results, uncomment the last to list the prime numbers found
        print('Find all primes up to: ' + str(nbr) + ' using ' + str(num_tasks) + ' tasks.')
        print('Time elasped: ' + str(end) + ' seconds')
        print('Number of primes found ' + str(total_primes))
        print('Comparisons done per node, min: {}, max: {}, delta: {}'.format(
                min(comparisons),
                max(comparisons),
                max(comparisons)-min(comparisons)
            ))
            
        return (nbr, num_tasks, end, total_primes, max(comparisons)-min(comparisons))
        

    results_summary = []
    
    print("Using {} processes in a multiprocessing Pool".format(num_processes))
    
    with mp.Pool(num_processes) as pool:
        for nbr in max_number:
            print("#\nBenchmarking for {}".format(nbr))
            
            print("\nRunning using implementation presented initially")
            results_summary.append(["basic", *benchmark(pool, nbr, num_processes, runNaively)])

            print("\nRunning using implementation presented initially, but halving the task size")
            results_summary.append(["halved", *benchmark(pool, nbr, num_processes*2, runNaively)])

            print("\nRunning using implementation with a work distribution heuristic")
            results_summary.append(["heuristic", *benchmark(pool, nbr, num_processes, runWithHeuristic)])

    print("\nSummary of the benchmarking:\n")

    print("| {:9} | {:9} | {:5} | {:8} | {:6} | {:12} |".format("Method", "Work size", "Tasks", "Time (s)", "Primes", "Tasks diff"))
    for result in results_summary:
        print("| {:9} | {:9} | {:>5} | {:>8} | {:>6} | {:>12} |".format(*[str(value) for value in result]))


if __name__ == "__main__":
    main()
