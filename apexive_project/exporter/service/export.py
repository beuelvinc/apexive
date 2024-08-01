from helper.helper import Helper


class ExportData:
    """
    This class exports data from PilotData
    """
    EXPORT_FILE_NAME = "export-logbook_template.csv"

    def __init__(self):
        self.helper = Helper(ExportData.EXPORT_FILE_NAME)

    def export(self) -> None:
        data = self.helper.read_data_from_database("aircraft")
        self.helper.export_data_to_csv(data)

        data = self.helper.read_data_from_database("flight")
        self.helper.export_data_to_csv(data)
