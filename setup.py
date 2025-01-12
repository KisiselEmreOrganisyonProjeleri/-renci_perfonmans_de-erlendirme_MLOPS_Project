from setuptools import find_packages, setup

def get_requirements(file_path:str)->list[str]: # Parametre string tipinde olacaktır ve return tipi liste içinde string tipinde elemanlar olacaktır
    """
    Bu fonksiyon gereken kütüphaneleri listenin elemanı olarak kayıt eder.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # dosya içindeki her satırı sıra sıra okur
        requirements = [req.replace('\n','')for req in requirements]
        return requirements

setup(
    name = 'ogrenci_perfonmans_degerlendirme',
    version = '0.0.1',
    author = 'emre',
    author_email = 'yunusemrek558@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('/workspaces/-renci_perfonmans_de-erlendirme_MLOPS_Project/requirements.txt')
)