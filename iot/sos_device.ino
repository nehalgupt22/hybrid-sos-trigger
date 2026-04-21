#include <Wire.h>
#include <MPU6050.h>
#include <SoftwareSerial.h>
#include <TinyGPS++.h>

MPU6050 mpu;
TinyGPSPlus gps;

// GPS (RX, TX)
SoftwareSerial gpsSerial(4, 3);

// GSM (RX, TX)
SoftwareSerial gsmSerial(8, 7);

const int buttonPin = 2;
const int buzzerPin = 9;

bool sosSent = false;
int threshold = 20000; // adjust based on sensitivity

void setup() {
  Serial.begin(9600);
  gpsSerial.begin(9600);
  gsmSerial.begin(9600);

  Wire.begin();
  mpu.initialize();

  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(buzzerPin, OUTPUT);

  Serial.println("System Ready");
}

void loop() {

  // manual SOS trigger
  if (digitalRead(buttonPin) == LOW && !sosSent) {
    triggerSOS("Manual Trigger");
  }

  // read accelerometer
  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);

  long totalAccel = abs(ax) + abs(ay) + abs(az);

  // motion-based trigger
  if (totalAccel > threshold && !sosSent) {
    triggerSOS("Motion Trigger");
  }

  delay(300);
}

// ---------- SOS FUNCTION ----------
void triggerSOS(String reason) {

  sosSent = true;

  // buzzer alert
  digitalWrite(buzzerPin, HIGH);
  delay(300);
  digitalWrite(buzzerPin, LOW);

  float latitude = 0.0, longitude = 0.0;
  unsigned long startTime = millis();

  // try GPS for 10 sec
  while (millis() - startTime < 10000) {
    while (gpsSerial.available()) {
      gps.encode(gpsSerial.read());
      if (gps.location.isValid()) {
        latitude = gps.location.lat();
        longitude = gps.location.lng();
        break;
      }
    }
  }

  // send SMS
  gsmSerial.println("AT+CMGF=1");
  delay(1000);

  gsmSerial.println("AT+CMGS=\"+918218387366\"");  // replace number
  delay(1000);

  gsmSerial.print("SOS Alert - ");
  gsmSerial.print(reason);
  gsmSerial.print("\nLocation: https://maps.google.com/?q=");
  gsmSerial.print(latitude, 6);
  gsmSerial.print(",");
  gsmSerial.print(longitude, 6);

  delay(500);
  gsmSerial.write(26); // CTRL+Z
  delay(5000);

  Serial.println("SOS sent");
}
