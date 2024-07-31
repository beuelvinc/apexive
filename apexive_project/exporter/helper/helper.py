import json
import os
from typing import Callable

from pilotlog_app.models import PilotData
from django.conf import settings
from django.db.models import Q


class Helper:
    """
    This class serving helper role for service class
    """

    def read_data_from_database(self) -> Callable[[], dict]:
        return self.__read_data_from_database

    @staticmethod
    def __read_data_from_database() -> dict:
        """
        Reads data from PilotData table where  table_name is  Aircraft or Flight
        :return:
        """
        try:
            return PilotData.objects.filter(Q(table="Aircraft") | Q(table="Flight"))
        except Exception as err:
            print(err)

    def export_data_to_csv(self, file_name: str, data: dict):
        """

        :param file_name: name of file to write
        :param data: data taht fetched from database
        :return: None
        """
        path_to_write = os.path.join(settings.BASE_DIR, "0_data", file_name)
        self.__delete_if_exists(path_to_write)
        self.__export_data_to_csv(file_name, data)

    def __export_data_to_csv(self, path: str, data: dict):
        """
        :param path: path of file to write data
        :param data: data from database
        :return: None
        """
        try:
            pass
        except Exception as err:
            print(err)

    def __delete_if_exists(self,file_path: str):
        """
        :param file_path: path of file to be deleted
        :return: None
        """
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted existing file: {file_path}")
        else:
            print(f"No file to delete: {file_path}")