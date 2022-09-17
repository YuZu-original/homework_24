import os


def get_file_lines(filepath: str) -> list[str]:
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        raise FileExistsError(f"File '{filepath}' not found or it's not file")
    
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().splitlines()
