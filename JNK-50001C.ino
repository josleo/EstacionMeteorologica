#define sensorPin  2 // pin 2 

void setup() {

 
  pinMode(sensorPin, INPUT_PULLUP);// define pin  as input for sensor
  Serial.begin(9600);// initialize serial monitor with 9600 baud.
}

void loop() {
  int sensor = digitalRead(sensorPin);
   Serial.println(sensor); 

 delay(300);

}
 