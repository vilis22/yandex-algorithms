class InvalidDataError(Exception):
    pass


def process_data(data: dict) -> None:
    if not isinstance(data, dict):
        raise InvalidDataError("Данные должны быть словарем")


if __name__ == "__main__":
    data = {}
    process_data(data)
