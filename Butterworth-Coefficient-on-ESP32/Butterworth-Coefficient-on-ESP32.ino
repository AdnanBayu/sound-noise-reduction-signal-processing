// File berikut merupakan contoh implementasi sebuah low-pass filter pada Arduino.
// Menggunakan input sinyal sinusoid buatan (sinyal tes)

double xn1 = 0;
double xn2 = 0;
double yn1 = 0;
double yn2 = 0;
int k = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  // Sinyal tes input
  double t = micros()/1.0e6;
  double xn = sin(2*PI*2*t) + 0.2*sin(2*PI*50*t);

  // Hitung sinyal terfilter dengan persamaan beda
  // double yn = 0.969*yn1 + 0.0155*xn + 0.0155*xn1;
  double yn = 1.955*yn1 - 0.956*yn2 + 0.00024132*xn + 0.00048264*xn1 + 0.00024132*xn2;

  delay(1);
  xn2 = xn1;
  yn2 = yn1;
  xn1 = xn;
  yn1 = yn;

  if(k % 3 == 0){
    // This extra conditional statement is here to reduce
    // the number of times the data is sent through the serial port
    // because sending data through the serial port
    // messes with the sampling frequency
  
    // Sinyal Output Ditampilkan
    Serial.print(2*xn);
    Serial.print(" ");
    Serial.println(2*yn);
  }
  k = k+1;
}
