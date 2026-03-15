class MyCustomError(Exception):
    pass


def cause_error():
    raise MyCustomError()
