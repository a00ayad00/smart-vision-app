import os

def mkdirs(dirs: list) -> None:
    for dir in dirs:
        if '.' in dir:
            dir = os.path.dirname(dir)
        os.makedirs(dir, exist_ok=True)