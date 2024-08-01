import csv
import os
from typing import Any, List, Dict
from django.conf import settings
from pilotlog_app.models import Aircraft, Airfield, Flight, ImagePic, LimitRules, MyQuery, MyQueryBuild, Pilot, \
    Qualification, SettingConfig


class Helper:
    """
    Helper class for various service-related tasks such as reading data from the database
    and exporting data to CSV files.
    """

    def __init__(self, file_name: str):
        """
        Initializes the Helper class with a specified file name for exporting data.

        :param file_name: Name of the file to export data to.
        """
        self.current_model = None
        self.path_to_write = os.path.join(settings.BASE_DIR, "0_data", file_name)
        self.__delete_if_exists(self.path_to_write)

    def read_data_from_database(self, model_name: str) -> List[Dict[str, Any]]:
        """
        Reads data from the specified database model.

        :param model_name: Name of the model to read data from.
        :return: A list of dictionaries containing the data from the database.
        """
        return self.__read_data_from_database(model_name)

    def __read_data_from_database(self, model_name: str) -> List[Dict[str, Any]]:
        """
        Internal method to read data from the specified database model.

        :param model_name: Name of the model to read data from.
        :return: A list of dictionaries containing the data from the database.
        """
        try:
            self.current_model = model_name
            model = self.__get_model().get(model_name)
            return model.objects.all()
        except Exception as err:
            print(f"Error occurred while reading data from the database: {err}")

    def export_data_to_csv(self, data: List[Any]):
        """
        Exports the given data to a CSV file.

        :param data: List of data objects fetched from the database.
        :return: None
        """
        self.__export_data_to_csv(data)

    def __export_data_to_csv(self, data: List[Any]):
        """
        Internal method to export data to a CSV file.

        :param data: List of data objects from the database.
        :return: None
        """
        try:
            with open(self.path_to_write, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([])
                writer.writerow([f"Information about {self.current_model}"])
                writer.writerow([])

                if not data:
                    print("No data to write to CSV.")
                    return

                fieldnames, metadata_keys = self.__generate_keys(data[0].meta)
                dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                dict_writer.writeheader()

                for buffer in data:
                    row = {
                        'user_id': buffer.user_id,
                        'guid': buffer.guid,
                        'platform': buffer.platform,
                        '_modified': buffer._modified,
                    }
                    meta_json = buffer.meta

                    for key in metadata_keys:
                        row[key] = meta_json.get(key, "")

                    dict_writer.writerow(row)

        except Exception as err:
            print(f"Error occurred while exporting data to CSV: {err}")

    @staticmethod
    def __delete_if_exists(file_path: str):
        """
        Deletes the file at the specified path if it exists.

        :param file_path: Path of the file to be deleted.
        :return: None
        """
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted existing file: {file_path}")
        else:
            print(f"No file to delete: {file_path}")

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

    @staticmethod
    def __generate_keys(data: dict) -> (List[str], List[str]):
        """
        Generates the field names for the CSV file, including keys from the meta field.

        :param data: Dictionary containing meta data.
        :return: A tuple containing a list of field names and a list of meta keys.
        """
        meta_keys = list(data.keys())
        fieldnames = ['user_id', 'guid', 'platform', '_modified'] + meta_keys
        return fieldnames, meta_keys
