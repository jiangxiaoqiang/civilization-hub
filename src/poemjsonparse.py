import json
import os


class PoemJsonParse:

    def parse(self):
        print("dd")

    def read_file(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            return files

    def read_json(self, path):
        try:
            with open(path, "r") as load_file:
                load_file_content = json.load(load_file)
                print(load_file_content)
        except Exception as e:
            print(e)
