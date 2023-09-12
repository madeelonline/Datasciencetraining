from setuptools import setup ,find_packages


def get_requirements(file_path):
    requirements = []

    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements





setup(

name = "datasciencetestproject",
version = '0.0.1',
author='nasir hussain',
author_email='nhussain@metpi.edu.pk',
packages=find_packages(),
install_requirements = get_requirements('requirements.txt')


)