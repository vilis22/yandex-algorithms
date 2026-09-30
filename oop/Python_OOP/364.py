class TextsComparison:
    @staticmethod
    def get_list_strings(file_path):
        with open(file_path, encoding="utf-8") as file:
            return file.readlines()

    def __call__(self, file_path1, file_path2, *args, **kwargs):
        doc1 = self.get_list_strings(file_path1)
        doc2 = self.get_list_strings(file_path2)

        if doc1 == doc2:
            return "Документы полностью соответствуют"

        inconsistencies = {}

        for line_number, (line1, line2) in enumerate(zip(doc1, doc2), start=1):
            if line1 != line2:
                inconsistencies[line_number] = [hash(line1), hash(line2)]

        match_percent = 100 - len(inconsistencies) / len(doc1) * 100
        return inconsistencies, match_percent
