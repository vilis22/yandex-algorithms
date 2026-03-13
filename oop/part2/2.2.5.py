class DateConverter:
    @staticmethod
    def to_iso_format(date_string):
        return "-".join(date_string.split(".")[::-1])

    @staticmethod
    def from_iso_format(date_string):
        return ".".join(date_string.split("-")[::-1])
