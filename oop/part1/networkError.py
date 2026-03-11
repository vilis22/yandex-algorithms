class NetworkError(Exception):
    pass


class HttpError(NetworkError):
    pass


def get_network_error_classes(classes_list):
    subclasses_list = [obj for obj in classes_list if issubclass(obj, NetworkError)]
    return subclasses_list
