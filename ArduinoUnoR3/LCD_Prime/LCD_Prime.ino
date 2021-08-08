//I'm trying to get LCD to print out Primes
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

unsigned long count = 2; //Start at 2- 1 doesn't count
int printDelay = 500; //Minimum prime number delay

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("Finding Primes");
}

void loop() {
  unsigned long start = millis();
  if(isPrime(count)) {
    //Serial.println(count);
    lcd.setCursor(0, 1);
    lcd.print(count);
    
    if(millis() - start < printDelay) {
      delay(abs(printDelay - (millis() - start)));
    }
  }
  count++;
}

boolean isPrime(unsigned long x) {
  boolean prime = true;
  
  for(unsigned long i = 2; i <= x/2; i++) { //Loop every number up to half
    if(x % i == 0) { //If it's divisible...
      prime = false; //It isn't prime!
      break;
    }
  }
  
  return prime;
}
