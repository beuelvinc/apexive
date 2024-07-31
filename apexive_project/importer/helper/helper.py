import json
import os
from pilotlog_app.models import Aircraft, Airfield, Flight, ImagePic, LimitRules, MyQuery, MyQueryBuild, Pilot, Qualification, SettingConfig
from django.conf import settings


class Helper:
    """
    This class serving helper role for service class
    """
    def read_data_from_file(self, file_name: str) -> dict:
        return self.__read_data_from_file(file_name)

    def __read_data_from_file(self, file_name: str) -> dict:
        """
        Read data from given file
        :param file_name: name of file to read
        :return: data that read
        """
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
        """
        Data to be inserted to database table
        :param data: data that read from json file
        :return: None
        """
        try:
            for entry in data:
                # Convert table name to lowercase for case-insensitive matching
                table_name = entry['table'].lower()
                model = self.__get_model().get(table_name)
                if model:
                    model.objects.create(
                        user_id=entry['user_id'],
                        guid=entry['guid'],
                        platform=entry['platform'],
                        _modified=entry['_modified'],
                        meta=entry['meta']
                    )
                else:
                    print(f"No model found for table name: {entry['table']}")
        except Exception as err:
            print(err)
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
