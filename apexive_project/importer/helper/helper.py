import json
import os
from pilotlog_app.models import PilotData
from django.conf import settings


class Helper:
    """
    This class serving helper role for service class
    """
    def read_data_from_file(self, file_name: str) -> dict:
        return self.__read_data_from_file(file_name)

    def __read_data_from_file(self, file_name: str) -> dict:
        try:
            with open(os.path.join(settings.BASE_DIR, "0_data", file_name), encoding="utf-8") as f:
                data = f.read().replace("\\", "")
                json_data = json.loads(data)
            return json_data
        except Exception as err:
            print(err)

    def insert_data_to_db(self, data: dict) -> None:
        self.__insert_data_to_db(data)

    def __insert_data_to_db(self, data: dict) -> None:
        try:
            for entry in data:
                PilotData.objects.create(
                    user_id=entry['user_id'],
                    guid=entry['guid'],
                    platform=entry['platform'],
                    table = entry['table'],
                    _modified=entry['_modified'],
                    meta=entry['meta']
                )
        except Exception as err:
            print(err)

    # @staticmethod
    # def __get_model():
    #     return {
    #         'Aircraft': Aircraft,
    #         'Flight': Flight
    #     }
