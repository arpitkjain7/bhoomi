/*
 * Copyright @bhoomi
 * End to end IoT based hydroponic system.
 * [Arpit Jain]
*/
// Import libraries
#include <OneWire.h>
#include <DallasTemperature.h>
#include <Wire.h>

//define default values
#define SOUND_SPEED 0.03313
#define CM_TO_INCH 0.393701

//initiate variables
const int trigPin = 5;
const int echoPin = 18;
long duration;
float distanceCm;
float distanceInch;
struct waterLevel
{
  float waterLevelinCM;
  float waterLevelinInch;
} waterLevelObj;
// GPIO where the DS18B20 is connected to
const int oneWireBus = 4;
struct temperature
{
  float temperatureInC;
  float temperatureInF;
} temperatureObj;
int sensorValue = 0;
float tdsValue = 0;
float Voltage = 0;
float ph_calibration_value = 20.27; //20.24 - 0.7; //21.34 - 0.7
int phval = 0;
unsigned long int avgval;
int buffer_arr[10], temp;
float ph_value;

OneWire oneWire(oneWireBus);
DallasTemperature sensors(&oneWire);

void getWaterLevel()
{
  //  struct waterLevel waterLevelInstance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance
  distanceCm = duration * SOUND_SPEED / 2;

  // Convert to inches
  distanceInch = distanceCm * CM_TO_INCH;
  waterLevelObj.waterLevelinCM = distanceCm;
  waterLevelObj.waterLevelinInch = distanceInch;
  //  return waterLevelInstance;
}

void getWaterTemperature()
{
  sensors.requestTemperatures();
  float temperatureC = sensors.getTempCByIndex(0);
  float temperatureF = sensors.getTempFByIndex(0);
  temperatureObj.temperatureInC = temperatureC;
  temperatureObj.temperatureInF = temperatureF;
}

float getWaterHardness()
{
  sensorValue = analogRead(39);
  //Convert analog reading to Voltage
  Voltage = sensorValue * (3.3 / 4095);
  //Convert voltage value to TDS value
  float tds = (133.42 * Voltage * Voltage * Voltage - 255.86 * Voltage * Voltage + 857.39 * Voltage) * 0.5;
  return tds;
}

float getPhValue()
{
  for (int i = 0; i < 10; i++)
  {
    buffer_arr[i] = analogRead(34);
    delay(30);
  }
  for (int i = 0; i < 9; i++)
  {
    for (int j = i + 1; j < 10; j++)
    {
      if (buffer_arr[i] > buffer_arr[j])
      {
        temp = buffer_arr[i];
        buffer_arr[i] = buffer_arr[j];
        buffer_arr[j] = temp;
      }
    }
  }
  avgval = 0;
  for (int i = 2; i < 8; i++)
    avgval += buffer_arr[i];
  float volt = (float)avgval * (3.3 / 4095.0 / 6);
  float ph_act = -5.70 * volt + ph_calibration_value;
  return ph_act;
}
void setup()
{
  Serial.begin(115200);     // Starts the serial communication
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT);  // Sets the echoPin as an Input
  sensors.begin();          // Start the DS18B20 sensor
  Wire.begin();
}

void loop()
{
  // Get water level
  getWaterLevel();
  Serial.println(" --- Water Level --- ");
  Serial.printf("Distance = %fcm\n", waterLevelObj.waterLevelinCM);
  Serial.printf("Distance = %finch\n", waterLevelObj.waterLevelinInch);
  getWaterTemperature();
  Serial.println(" --- Water Temperature --- ");
  Serial.printf("Temperature in Celsius = %fºC\n", temperatureObj.temperatureInC);
  Serial.printf("Temperature in Farenheit = %fºF\n", temperatureObj.temperatureInF);
  tdsValue = getWaterHardness();
  Serial.println(" --- Water TDS Level --- ");
  Serial.printf("TDS Value = %f ppm\n", tdsValue);
  ph_value = getPhValue();
  Serial.println(" --- Water pH Level --- ");
  Serial.printf("pH Val = %f\n", ph_value);
  delay(5000);
}
