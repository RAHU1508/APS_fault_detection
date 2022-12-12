from setuptools import find_packages, setup

def get_requirements():
    pass

setup(
    name = 'sensor',
    version = '0.0.1',
    author = 'rahulkumar',
    author_email = 'rsk.150896@gmail.com',
    packages = find_packages(), #__init__.py file should be there in our 'sensor' folder in order for find_packages() to identify which source code to convert into library format
    install_requires = get_requirements(), #get_requirements() function is needed for other libraries required for this project
)