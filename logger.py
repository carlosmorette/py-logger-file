from datetime import datetime


class Logger:
    default_file_name = datetime.now().strftime("%Y%m%d%H%M%S")
    default_file_extension = "txt"

    def __init__(self, file: str = None, extension: str = None):
        self.filename = self.default_file_name if file is None else file
        self.extension_file = self.default_file_extension if extension is None else extension

    def __call__(self, message: str):
        print(message)
        full_filename = "{}.{}".format(self.filename, self.extension_file)

        with open(full_filename, "a") as out_file:
            out_file.write(message + "\n")

