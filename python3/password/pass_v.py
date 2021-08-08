#Experiment Password

import pass_g

u_input = pass_g.pass_g_output
print(u_input)

#count
#l_pass = len(u_input)
#print(l_pass)

u_input_list = list(u_input)

abc = "abcdefghijklmnopqrstuvwxyz"
ABC = abc.upper()
s123 = "0123456789"
#spec = """!@#$%^&*()_+[]\;',./{}|:"<>?"""

abc_list = list(abc)
ABC_list = list(ABC)
s123_list = list(s123)
#@spec_list = list(spec)

abc_conv = []
ABC_conv = []
s123_conv = []
#spec_conv = []

for x in abc_list:
    conv = ord(x)
    abc_conv.append(conv)
for x in ABC_list:
    conv = ord(x)
    ABC_conv.append(conv)
for x in s123_list:
    conv = ord(x)
    s123_conv.append(conv)
#for x in spec_list:
#    conv = ord(x)
#    spec_conv.append(conv)

abc_dict = dict(zip(abc_list, abc_conv))
#97 to 122
ABC_dict = dict(zip(ABC_list, ABC_conv))
#65 to 90
s123_dict = dict(zip(s123_list, s123_conv))
#49 to 57
#spec_dict = dict(zip(spec_list, spec_conv))

rev_conv = []

for x in range(0, 301):
    conv = chr(x)
    #print(conv)
    rev_conv.append(conv)

#print(s123_dict)

rev_conv2 = []

for x in rev_conv:
    conv = ord(x)
    #print(conv)
    rev_conv2.append(conv)

whole_dict = dict(zip(rev_conv2, rev_conv))
#print(whole_dict)

dump = []
dump2 = []
key = 0

for x in u_input_list:
    conv = ord(x)
    conv = (conv + key)
    dump.append(conv)
print(dump)

for x in dump:
    conv = chr(x - key)
    dump2.append(conv)
print(dump2)

conv_pass = "".join(dump2)
print(conv_pass)

#u_input_sum = sum(dump)
#print(u_input_sum)

#// is division leaving the remainder off and % is division only showing remainder

#prob = u_input_sum // l_pass
#prob2 = u_input_sum % l_pass
#print(prob, prob2)


#for x in dump:
#    if x in ABC_conv:
#        print("Good Uppercase")

#for x in dump:
#    if x in abc_conv:
#        print("Good Lowercase")

#for x in dump:
#    if x in s123_conv:
#        print("Good Number")

sea_A = set(dump) & set(ABC_conv)
sea_a = set(dump) & set(abc_conv)
sea_123 = set(dump) & set(s123_conv)

sea_A_sum = sum(sea_A)
sea_a_sum = sum(sea_a)
sea_123_sum = sum(sea_123)

if sea_123_sum > 0:
    print("Good Number")
else:
    print("Bad Number")
if sea_A_sum > 0:
    print("Good Uppercase")
else:
    print("Bad Uppercase")
if sea_a_sum > 0:
    print("Good Lowercase")
else:
    print("Bad Lowercase")