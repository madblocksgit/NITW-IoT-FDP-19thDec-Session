int moisture_sensor=A0;

void setup() // one-time executable
{
  pinMode(moisture_sensor,INPUT);
  Serial.begin(9600); // speed of UART - 9600
}

void loop() // logic - iterative loop - infinite - power goes off
{
  // read the data from sensor
  int sensor_value=analogRead(moisture_sensor);
  Serial.print("#"); // Start of the Data Frame
  Serial.print(sensor_value); // send sensor value
  Serial.print("~"); // End of the Data Frame
  Serial.println(); // New line
  delay(5000);// 5 seconds
}
