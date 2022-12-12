from setuptools import find_packages, setup
from typing import List

#listing down all the installable library names from requirements.txt file to requirement_list 
REQUIREMENT_FILE_NAME='requirements.txt'
HYPHEN_E_DOT = "-e ."
def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list] #in order to change line, '\n' is invisbly present in the requirements.txt file at the end of each line, we want to remove that

    if HYPHEN_E_DOT in requirement_list: #-e . is not a library, we don't want to include it in our list of libraries
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(
    name = "sensor",
    version = "0.0.1",
    author = "rahulkumar",
    author_email = "rsk.150896@gmail.com",
    packages = find_packages(), #__init__.py file should be there in our 'sensor' folder in order for find_packages() to identify which source code to convert into library format
    install_requires = get_requirements(), #get_requirements() function is needed for other libraries required for this project
)