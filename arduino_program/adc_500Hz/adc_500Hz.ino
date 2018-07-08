#include <avr/io.h>
#include <avr/interrupt.h>

volatile boolean flag = false;
//volatile int i = 0;

void setup() {

  // initialize Timer1
  cli();
  TCCR1A = 0;
  TCCR1B = 0;

  // set compare match register to desired timer count: 500Hz 249 1kHz
  OCR1A = 499;
  // turn on CTC mode:
  TCCR1B |= (1 << WGM12);
  // Set CS10 and CS12 bits for 64 prescaler:
  TCCR1B |= (1 << CS10);
  TCCR1B |= (1 << CS11);
  // enable timer compare interrupt:
  TIMSK1 |= (1 << OCIE1A);
  // enable global interrupts:


  Serial.begin(115200); // set the baud rate

  delay(500);

  sei();
}


void loop() {
  if(Serial.available()){
    flag = true;
  }
  else{
    flag=false;
  }
}

ISR(TIMER1_COMPA_vect){    

  if(flag==true){ 
//    Serial.print(analogRead(0));
//    Serial.print(",");  
//    Serial.print(analogRead(1)); 
//    Serial.print(","); 
//    Serial.print(analogRead(2)); 
//    Serial.print(",");  
//    Serial.print(analogRead(3)); 
//    Serial.print(",");  
//    Serial.print(analogRead(4)); 
//    Serial.print(",");   
    Serial.print(analogRead(0));
    Serial.print(" ");
   Serial.println(analogRead(1)); 
  }
}



