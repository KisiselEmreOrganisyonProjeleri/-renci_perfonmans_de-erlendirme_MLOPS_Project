import os
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    yaml dosyayı okur ve return eder.

    Parametre: path_to_yaml -> dosya yolunu temsil eder
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(yaml_file)
    except BoxValueError:
        raise ValueError('yaml dosyasının içi boş')
    except Exception as e:
        raise e
@ensure_annotations
def create_directories(path_to_directories:list, verbose = True):
    """
    Verilen klasörleri yaratır
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)

@ensure_annotations
def get_size(path: Path) -> str:
    'KB olarak dosya boyutunu döndürür'
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb}kb"