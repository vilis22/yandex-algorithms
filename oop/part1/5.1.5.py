class JsonExporter:
    def export(self, data):
        return f"Экспорт в JSON: {data}"


class CsvExporter:
    def export(self, data):
        return f"Экспорт в CSV: {data}"


def export_data(exporter, data):
    return exporter.export(data)
