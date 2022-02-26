from core.crud.position_data_crud import CRUDPositionData

# from datetime import datetime


def create_target_records(target_position_record: list):
    position_data = CRUDPositionData().read_all()
    if len(position_data) == 0:
        for item in target_position_record:
            CRUDPositionData().create(**item)
    else:
        pass


def main():
    target_position_record = [
        {
            "water_temperature": "HIGH",
            "tds_level": "HIGH",
            "ph_level": "HIGH",
        },
        {
            "water_temperature": "HIGH",
            "tds_level": "HIGH",
            "ph_level": "LOW",
        },
        {
            "water_temperature": "HIGH",
            "tds_level": "HIGH",
            "ph_level": "NORMAL",
        },
        {
            "water_temperature": "HIGH",
            "tds_level": "LOW",
            "ph_level": "HIGH",
        },
        {
            "water_temperature": "HIGH",
            "tds_level": "LOW",
            "ph_level": "LOW",
        },
        {
            "water_temperature": "HIGH",
            "tds_level": "LOW",
            "ph_level": "NORMAL",
        },
        {
            "water_temperature": "HIGH",
            "tds_level": "NORMAL",
            "ph_level": "HIGH",
        },
        {
            "water_temperature": "HIGH",
            "tds_level": "NORMAL",
            "ph_level": "LOW",
        },
        {
            "water_temperature": "HIGH",
            "tds_level": "NORMAL",
            "ph_level": "NORMAL",
        },
        {
            "water_temperature": "LOW",
            "tds_level": "HIGH",
            "ph_level": "HIGH",
        },
        {
            "water_temperature": "LOW",
            "tds_level": "HIGH",
            "ph_level": "LOW",
        },
        {
            "water_temperature": "LOW",
            "tds_level": "HIGH",
            "ph_level": "NORMAL",
        },
        {
            "water_temperature": "LOW",
            "tds_level": "LOW",
            "ph_level": "HIGH",
        },
        {
            "water_temperature": "LOW",
            "tds_level": "LOW",
            "ph_level": "LOW",
        },
        {
            "water_temperature": "LOW",
            "tds_level": "LOW",
            "ph_level": "NORMAL",
        },
        {
            "water_temperature": "LOW",
            "tds_level": "NORMAL",
            "ph_level": "HIGH",
        },
        {
            "water_temperature": "LOW",
            "tds_level": "NORMAL",
            "ph_level": "LOW",
        },
        {
            "water_temperature": "LOW",
            "tds_level": "NORMAL",
            "ph_level": "NORMAL",
        },
        {
            "water_temperature": "NORMAL",
            "tds_level": "HIGH",
            "ph_level": "HIGH",
        },
        {
            "water_temperature": "NORMAL",
            "tds_level": "HIGH",
            "ph_level": "LOW",
        },
        {
            "water_temperature": "NORMAL",
            "tds_level": "HIGH",
            "ph_level": "NORMAL",
        },
        {
            "water_temperature": "NORMAL",
            "tds_level": "LOW",
            "ph_level": "HIGH",
        },
        {
            "water_temperature": "NORMAL",
            "tds_level": "LOW",
            "ph_level": "LOW",
        },
        {
            "water_temperature": "NORMAL",
            "tds_level": "LOW",
            "ph_level": "NORMAL",
        },
        {
            "water_temperature": "NORMAL",
            "tds_level": "NORMAL",
            "ph_level": "HIGH",
        },
        {
            "water_temperature": "NORMAL",
            "tds_level": "NORMAL",
            "ph_level": "LOW",
        },
        {
            "water_temperature": "NORMAL",
            "tds_level": "NORMAL",
            "ph_level": "NORMAL",
        },
    ]
    create_target_records(target_position_record=target_position_record)
