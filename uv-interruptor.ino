#define sensorPin  2 // pin 2 
void setup() 
{

   // Robojax.com 20181110 NJK-5002C hall sensor
  pinMode(sensorPin, INPUT_PULLUP);// define pin  as input for sensor
  Serial.begin(9600);// initialize serial monitor with 9600 baud.
}

void loop() 
{
  float sensorVoltageUv; 
  float sensorValueUv;
  
  //interruptor magnetico
  int Interruptor = digitalRead(sensorPin);// read pin 2 and put the result in the "sensed" variable

  sensorValueUv = analogRead(A1);
  sensorVoltageUv = sensorValue/4095*3.3; //3.3

  Serial.print(Interruptor); //afficher la valeur analogique
  Serial.print("-");
  Serial.print("sensor reading = ");
  Serial.print(sensorValueUv);
  Serial.print("-");
  Serial.print("sensor voltage = ");
  Serial.print(sensorVoltageUv);
  Serial.println(" V");
  delay(1000);


}
