import csv
import os
from itertools import chain
from typing import Any
from django.conf import settings
from pilotlog_app.models import Aircraft, Airfield, Flight, ImagePic, LimitRules, MyQuery, MyQueryBuild, Pilot, \
    Qualification, SettingConfig


class Helper:
    """
    This class serving helper role for service class
    """

    def read_data_from_database(self,model_name: str) -> list[dict[str, str | Any]]:
        return self.__read_data_from_database(model_name)

    def __read_data_from_database(self, model_name: str) -> list[dict[str, str | Any]]:
        """
        Reads data from DB tables
        :return:
        """
        try:
            model = self.__get_model().get(model_name)
            return model.objects.all()
        except Exception as err:
            print(err)

    def export_data_to_csv(self, data: dict, file_name: str, ):
        """

        :param file_name: name of file to write
        :param data: data taht fetched from database
        :return: None
        """
        path_to_write = os.path.join(settings.BASE_DIR, "0_data", file_name)
        # self.__delete_if_exists(path_to_write)
        self.__export_data_to_csv(path_to_write, data)

    def __export_data_to_csv(self, path: str, data: dict):
        """
        :param path: path of file to write data
        :param data: data from database
        :return: None
        """
        try:

            with open(path, 'w', newline='') as csvfile:
                fieldnames = ['user_id', 'guid', 'platform', '_modified', 'meta']
                writer = csv.writer(csvfile)
                writer.writerow(["NOOWW NEW"])
                for buffer in data:
                    writer.writerow({
                        'user_id': buffer.user_id,
                        'guid': buffer.guid,
                        'platform': buffer.platform,
                        '_modified': buffer._modified,
                        'meta': buffer.meta
                    })

        except Exception as err:
            print(err)

    @staticmethod
    def __delete_if_exists(file_path: str):
        """
        :param file_path: path of file to be deleted
        :return: None
        """
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted existing file: {file_path}")
        else:
            print(f"No file to delete: {file_path}")

    @staticmethod
    def __get_model():
        return {
            'aircraft': Aircraft,
            'airfield': Airfield,
            'flight': Flight,
            'imagepic': ImagePic,
            'limitrules': LimitRules,
            'myquery': MyQuery,
            'myquerybuild': MyQueryBuild,
            'pilot': Pilot,
            'qualification': Qualification,
            'settingconfig': SettingConfig
        }