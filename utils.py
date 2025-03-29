import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
# from src import logger
from pathlib import Path


def read_yaml(yaml_path: Path) -> ConfigBox:
    try:
        with open(yaml_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            # logger.info(f"The file: {yaml_path} loaded successfully...")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

def mkdirs(dirs: list) -> None:
    for dir in dirs:
        if '.' in dir:
            dir = os.path.dirname(dir)
        os.makedirs(dir, exist_ok=True)