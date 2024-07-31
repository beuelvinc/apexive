import json
import os
from pilotlog_app.models import PilotData
from django.conf import settings


class Helper:
    """
    This class serving helper role for service class
    """

    def read_data_from_database(self):
        return self.__read_data_from_database

    def __read_data_from_database(self):
        try:
            pass
        except Exception as err:
            print(err)

    def export_data_to_csv(self, file_name: str, data: dict):
        self.__export_data_to_csv(file_name, data)

    def __export_data_to_csv(self, file_name: str, data: dict):
        path_to_write = os.path.join(settings.BASE_DIR, "0_data", file_name)
        try:
            pass
        except Exception as err:
            print(err)
