const int ledPin = 12;
void setup() {
  Serial.begin(9609);
  pinMode (ledPin, oUTPUT);
}
void loop() {
  if (Serial . available() > 0) {
    char command = Serial.read();
    if (command == 'y') {
      digitalWrite (ledPin, HIGH);
    } else if (command == 's') {
    digitalWrite (ledPin, LOW);
    }
  }
}
