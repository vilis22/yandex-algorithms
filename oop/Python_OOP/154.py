import json


class ParseJson:
    @staticmethod
    def full_parse():
        with open("to-do_list.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    @staticmethod
    def parse_key(key):
        keys = key.lower().split(".")
        data = ParseJson.full_parse()
        data_lower = {k.lower(): v for k, v in data.items()}

        if len(keys) == 1:
            return data_lower.get(keys[0], "Данные не найдены")
        elif len(keys) == 2:
            first = data_lower.get(keys[0])

            if first is None or not isinstance(first, dict):
                return "Данные не найдены"

            first_lower = {k.lower(): v for k, v in first.items()}
            return first_lower.get(keys[1], "Данные не найдены")
        else:
            return "Данные не найдены"


print(ParseJson.parse_key("воскРесенье.рЫжик"))
