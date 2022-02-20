from turtle import clear
import requests
import json
import random
import pandas as pd
from datetime import datetime
from datetime import timedelta


class APIInterface:
    @staticmethod
    def post(route, data=None, headers=None):
        try:
            url = route
            print("POST request sent")
            print(f"url = {url}, data = {data}")
            response = requests.post(url, json=data, headers=headers)
            if response.status_code >= 400:
                raise Exception(
                    f"Call to {route} failed with {response.status_code} and response {response.text}"
                )
            return json.loads(response.text), response.status_code
        except Exception as error:
            print(f"Error in POST API request: {error}")


# # # for i in range(1135):
# # #     water_temp = round(random.uniform(14.00, 34), 2)
# # #     water_level = round(random.uniform(2, 14), 0)
# # #     ph = round(random.uniform(3, 10), 1)
# # #     tds = round(random.uniform(200, 900), 0)
# # #     air_temp = round(random.uniform(14.00, 36.00), 2)
# # #     url = "http://localhost:8000/bhoomi/sensor/save_data"
# # #     route = f"{url}?water_temperature={water_temp}&air_temperature={air_temp}&tds_level={tds}&ph_level={ph}&water_level={water_level}"
# # #     resp = APIInterface().post(route=route)
# # #     print(f"Response: {resp} for request#: {i}")


# # # df = pd.read_csv("positions.csv")
# # # for index, items in df.iterrows():
# # #     water_temp = items["water_temp"]
# # #     tds = items["tds"]
# # #     ph = items["ph"]
# # #     url = "http://localhost:8000/bhoomi/target/save_data"
# # #     route = f"{url}?water_temperature={water_temp}&tds_level={tds}&ph_level={ph}"
# # #     resp = APIInterface().post(route=route)
air_temp_low = 17
air_temp_high = 28
water_temp_low = 17
water_temp_high = 26
ph_level_low = 5.8
ph_level_high = 6.8
tds_level_low = 560
tds_level_high = 840
water_level_low = 5
water_level_high = 10
url = "http://localhost:8000/bhoomi/sensor/get"
position_url = "http://localhost:8000/bhoomi/target/get_position"
knn_url = "http://localhost:8000/bhoomi/knn/historical_data"
sensor_data, resp_code = APIInterface().post(route=url)
today = datetime.now()
n = 25
recorded_date = today - timedelta(days=n)
print(recorded_date)
for data in sensor_data:
    recorded_date = recorded_date + timedelta(minutes=2)
    print(recorded_date)
    print(f"{data=}")
    recorded_water_temperature = data.get("water_temperature")
    if recorded_water_temperature > water_temp_high:
        water_temperature = "HIGH"
    elif recorded_water_temperature < water_temp_low:
        water_temperature = "LOW"
    else:
        water_temperature = "NORMAL"
    recorded_air_temperature = data.get("air_temperature")
    recorded_tds_level = data.get("tds_level")
    if recorded_tds_level > tds_level_high:
        tds_level = "HIGH"
    elif recorded_tds_level < tds_level_low:
        tds_level = "LOW"
    else:
        tds_level = "NORMAL"
    recorded_ph_level = data.get("ph_level")
    if recorded_ph_level > ph_level_high:
        ph_level = "HIGH"
    elif recorded_ph_level < ph_level_low:
        ph_level = "LOW"
    else:
        ph_level = "NORMAL"
    recorded_water_level = data.get("water_level")
    route = f"{position_url}?water_temperature={water_temperature}&tds_level={tds_level}&ph_level={ph_level}"
    resp, rep_code = APIInterface().post(route=route)
    target = resp.get("position_id")
    route = f"{knn_url}?water_temperature={recorded_water_temperature}&air_temperature={recorded_air_temperature}&tds_level={recorded_tds_level}&ph_level={recorded_ph_level}&water_level={recorded_water_level}&target={target}&recorded_date={recorded_date}"
    resp, rep_code = APIInterface().post(route=route)
    print(resp_code)
# n = 25
# today = datetime.now()
# recorded_date = today - timedelta(days=n)
# print(recorded_date)
# recorded_date = recorded_date + timedelta(minutes=2)
# route = f"{knn_url}?water_temperature={23}&air_temperature={23}&tds_level={233}&ph_level={2}&water_level={32}&target={1}&recorded_date={recorded_date}"
# resp, rep_code = APIInterface().post(route=route)
