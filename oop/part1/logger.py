class Logger:
    def log(self, message):
        return f"[LOG]: {message}"


class TimestampLogger(Logger):
    def log(self, message):
        return super().log(message) + " (timestamp)"
