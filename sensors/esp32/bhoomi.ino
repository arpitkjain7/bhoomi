/*
 * Copyright @bhoomi
 * End to end IoT based hydroponic system.
 * [Arpit Jain]
*/
// Import libraries
#include <OneWire.h>
#include <DallasTemperature.h>
#include <Wire.h>
#include <DHT.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

//define default values
#define SOUND_SPEED 0.03313
#define CM_TO_INCH 0.393701

//initiate variables
const char *ssid = "R.K.Jain";
const char *password = "Arpit@123";
const char *serverName = "http://192.168.1.100:8000/bhoomi/sensor/save_data";
const int trigPin = 5;
const int echoPin = 18;
long duration;
float distanceCm, distanceInch;
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
int sensorValue = 0, phval = 0, buffer_arr[10], temp;
float tdsValue = 0, Voltage = 0, ph_calibration_value = 20.27; //20.24 - 0.7; //21.34 - 0.7
unsigned long int avgval;
float ph_value, air_temp, air_humidity;

WiFiClient client;
OneWire oneWire(oneWireBus);
DallasTemperature waterTempSensor(&oneWire);
DHT dht(16, DHT11);

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
  waterTempSensor.requestTemperatures();
  float temperatureC = waterTempSensor.getTempCByIndex(0);
  float temperatureF = waterTempSensor.getTempFByIndex(0);
  temperatureObj.temperatureInC = temperatureC;
  temperatureObj.temperatureInF = temperatureF;
}

void getAirTemperature()
{
  air_humidity = dht.readHumidity();
  air_temp = dht.readTemperature();
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

void sendData(String water_temperature, String air_temperature, String tds_level, String ph_level, String water_distance)
{
  if (WiFi.status() == WL_CONNECTED)
  {
    WiFiClient client;
    HTTPClient http;
    // Your Domain name with URL path or IP address with path
    http.begin(client, serverName);
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    String httpRequest = "water_temperature=" + water_temperature + "&air_temperature=" + air_temperature + "&tds_level=" + tds_level + "&ph_level=" + ph_level + "&water_distance=" + water_distance;
    Serial.print(httpRequest);
    int httpResponseCode = http.POST(httpRequest);
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    String payload = "{}";
    if (httpResponseCode == 200)
    {
      payload = http.getString();
    }
    StaticJsonDocument<300> doc;
    auto error = deserializeJson(doc, payload);
    if (error)
    {
      Serial.print(F("deserializeJson() failed with code "));
      Serial.println(error.c_str());
      return;
    }
    const char *tdsRelayPosition = doc["tds_level"];
    const char *waterTempRelayPosition = doc["water_temperature"];
    const char *phRelayPosition = doc["ph_level"];
    int pos_id = doc["position_id"];
    Serial.print("HTTP Response payload: ");
    Serial.println(payload);
    Serial.println(tdsRelayPosition);
    http.end();
  }
  else
  {
    Serial.println("WiFi Disconnected");
  }
}
void setup()
{
  Serial.begin(115200);     // Starts the serial communication
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT);  // Sets the echoPin as an Input
  waterTempSensor.begin();  // Start the DS18B20 sensor
  Wire.begin();
  dht.begin();
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
  Serial.println(WiFi.localIP());
}

void loop()
{
  // Get water level
  getAirTemperature();
  Serial.println(" --- Air Condition --- ");
  Serial.printf("Air Temperature = %fºC\n", air_temp);
  Serial.printf("Humidity = %f\n", air_humidity);
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
  sendData((String)temperatureObj.temperatureInC, (String)air_temp, (String)tdsValue, (String)ph_value, (String)waterLevelObj.waterLevelinCM);
  Serial.println("******************************************");
  delay(20000);
}