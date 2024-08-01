import json
import os
from pilotlog_app.models import Aircraft, Airfield, Flight, ImagePic, LimitRules, MyQuery, MyQueryBuild, Pilot, Qualification, SettingConfig
from django.conf import settings


class Helper:
    """
    Helper class for various service-related tasks such as reading data from files
    and inserting data into database tables.
    """

    def read_data_from_file(self, file_name: str) -> dict:
        """
        Reads data from a specified file.

        :param file_name: Name of the file to read data from.
        :return: A dictionary containing the data read from the file.
        """
        return self.__read_data_from_file(file_name)

    def __read_data_from_file(self, file_name: str) -> dict:
        """
        Internal method to read data from a specified file.

        :param file_name: Name of the file to read data from.
        :return: A dictionary containing the data read from the file.
        """
        try:
            with open(os.path.join(settings.BASE_DIR, "0_data", file_name), encoding="utf-8") as f:
                data = f.read().replace("\\", "")
                json_data = json.loads(data)
            return json_data
        except Exception as err:
            print(err)

    def insert_data_to_db(self, data: dict) -> None:
        """
        Inserts data into the database tables.

        :param data: Dictionary containing the data to be inserted into the database.
        :return: None
        """
        self.__insert_data_to_db(data)

    def __insert_data_to_db(self, data: dict) -> None:
        """
        Internal method to insert data into the database tables.

        :param data: Dictionary containing the data to be inserted into the database.
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
        """
        Retrieves a dictionary mapping model names to model classes.

        :return: Dictionary mapping model names to model classes.
        """
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
