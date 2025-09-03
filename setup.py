""" It is basically a configuration file for project which specify the intallation of the project and what are the dependencies and basic info about project"""
""" The setup.py file is essential part for packaging and distributing the python projects.
It is used by setuptools   to define the configuration of your project as metadata , depenencies and more """
""" we can install this entire project using the pip install after specifying the setup.py"""
from setuptools import find_packages,setup # find_package scan the entire project and which ever folder contains __init__.py file it consider as package
from typing import List # 

def get_requirement()-> List[str]:
    """ This function return list of requirement"""
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt' ,'r') as file:
            # read lines from the file
            lines = file.readlines()
            for line in lines:
                # process each line
                requirement = line.strip() # remove the extra space
                if requirement and requirement != '-e .': # if not then add in list
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst
# setup the metadata
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ajay Sulya",
    author_email="ajaysulya06@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement()
)