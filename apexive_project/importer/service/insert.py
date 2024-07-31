from helper.helper import Helper

class InsertData:
    """
    This class inserts data to DB  tables
    """
    IMPORT_FILE_NAME = "import-pilotlog_mcc.json"

    def __init__(self):
        self.helper = Helper()

    def insert(self) -> None:
        data = self.helper.read_data_from_file(InsertData.IMPORT_FILE_NAME)
        self.helper.insert_data_to_db(data)

