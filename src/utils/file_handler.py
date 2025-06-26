def read_chat_log(file_path):
    """Read chat log file and return lines."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()