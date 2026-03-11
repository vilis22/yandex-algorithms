def get_count(data_structure):
    if isinstance(data_structure, (str, list, dict)):
        return len(data_structure)
