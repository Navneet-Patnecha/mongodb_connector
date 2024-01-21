from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirement(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.4"
REPO_NAME = "mongodb_connector"
PKG_NAME= "MongoDB-connect"
AUTHOR_USER_NAME = "Navneet-Patnecha"
AUTHOR_EMAIL = "navneetchippa@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Navneet-Patnecha/mongodb_connector",
    project_urls={
        "Bug Tracker": f"https://github.com/Navneet-Patnecha/mongodb_connector",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires = get_requirement("./requirements_dev.txt")
    )