import json


def build_data(file_name):
    data = []
    with open(file_name, encoding="utf-8") as f:
        r_data = json.load(f)
        for case_data in r_data.values():
            data.append(list(case_data.values()))
            print(data)
        return data


if __name__ == '__main__':
    build_data("../data/data.json")
