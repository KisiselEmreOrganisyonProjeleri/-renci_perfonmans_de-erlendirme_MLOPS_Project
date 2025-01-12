import os # Bizim dosyalarımızın yolllarını belirtmemizi sağlayan bir kütüphane
from pathlib import Path # String tipinde dosya yollarını Python'ın anlayacağı bir tipe çevirir (PATH)
import logging # Yapılan işlemlerin aşamalarını bilgi vermek amacıyla oluşturduğumuz kütüphanedir.

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s')
project_name = 'ogrenci_perfonmans_degerlendirme'

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'research/deneme1.ipynb',
    'templates/index.html',
    'main.py'
]
for filepath in list_of_files:
    filepath = Path(filepath) # yukarıdaki string tipindeki değerleri dosya_yolu tipine çevirdik
    filedir, filename = os.path.split(filepath) #filedir = src/{project_name} filename = __init__.py
    if filedir != '': # eğer içinde bir dosya varsa
        os.makedirs(filedir,exist_ok=True) # Eğer önceden bu isimle bir yol oluşturulduysa tekrardan oluşturulmak istenirse hata gelmesini sağlar.
        logging.info(f'Oluşturulan dosyanın yolu {filedir} ve oluşturulan dosya ismi {filename}dir')
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath == 0)):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Oluşturulan boş dosyanın yolu: {filepath}')
    else:
        logging.info(f'{filename} isimli dosya zaten mevcut tekrardan oluşturulamadı')
