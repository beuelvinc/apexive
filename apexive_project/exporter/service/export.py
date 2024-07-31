from helper.helper import Helper

class ExportData:
    """
    This class exports data from PilotData
    """
    IMPORT_FILE_NAME = "export-logbook_template.csv"

    def __init__(self):
        self.helper = Helper()

    def insert(self) -> None:
        data = self.helper.read_data_from_database()
        self.helper.export_data_to_csv(data, ExportData.IMPORT_FILE_NAME)

