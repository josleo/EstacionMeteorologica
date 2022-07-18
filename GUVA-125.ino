int uv=A0, lectura;

String riesgo="";
void setup() {
  Serial.begin(9600);

}

void loop() {
  lectura=analogRead(uv);
  //float voltaje=lectura * (5.0/1023.0);
  float voltaje=lectura * (3.3/669);
  int longOnda=map(lectura,0,669,0,1023);
  int indice=map(longOnda,0,1023,0,10);
  //Serial.println(lectura);
  //Serial.println("Voltaje:"+String(voltaje)+"V");
  //Serial.println("Rango:"+String(longOnda));
  if(indice==0){
    riesgo="0";
    
  }
  else if(indice==1 or indice ==2){
    riesgo="1";
  }
  else if(indice>=3 and indice <=5){
    riesgo="2";
  }
  else if(indice>=6 and indice <=7){
    riesgo="3";
  }
  else if(indice>=8 and indice <=10){
    riesgo="4";
  
  }
  else {
    riesgo="5";
  }
  //Serial.println("Indice UV:"+String(indice)+" - Rango:"+String(longOnda));
  Serial.print (riesgo);
  Serial.print("  ");
  Serial.print(lectura);
  Serial.print("Voltaje:"+String(voltaje)+"V");
  Serial.println("Rango:"+String(longOnda));

  delay(5000);
}