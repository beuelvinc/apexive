import os
from django.conf import settings
from django.db.models import Q
from pilotlog_app.models import Aircraft, Airfield, Flight, ImagePic, LimitRules, MyQuery, MyQueryBuild, Pilot, Qualification, SettingConfig



class Helper:
    """
    This class serving helper role for service class
    """

    def read_data_from_database(self) -> dict:
        return self.__read_data_from_database()

    @staticmethod
    def __read_data_from_database() -> dict:
        """
        Reads data from DB tables
        :return:
        """
        try:
            return PilotData.objects.filter(Q(table="Aircraft") | Q(table="Flight")).all()
        except Exception as err:
            print(err)

    def export_data_to_csv(self, data: dict, file_name: str,):
        """

        :param file_name: name of file to write
        :param data: data taht fetched from database
        :return: None
        """
        path_to_write = os.path.join(settings.BASE_DIR, "0_data", file_name)
        self.__delete_if_exists(path_to_write)
        self.__export_data_to_csv(path_to_write, data)

    def __export_data_to_csv(self, path: str, data: dict):
        """
        :param path: path of file to write data
        :param data: data from database
        :return: None
        """
        try:
            print(data)
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