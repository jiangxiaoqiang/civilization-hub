from src.poemjsonparse import PoemJsonParse

if __name__ == '__main__':
    try:
        folder_path = "/Users/dolphin/Documents/GitHub/chinese-poetry/json"
        poem_parser = PoemJsonParse()
        files = poem_parser.read_file(folder_path)
        for file in files:
            full_file_path = folder_path + "/" + file
            poem_parser.read_json(full_file_path)
    except Exception as e:
        print("dd" + e)
