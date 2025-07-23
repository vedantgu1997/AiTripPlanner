from setuptools import setup, find_packages # type: ignore
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirements_list: List[str] = []

    try:
        #open and read the requirements.txt file
        with open('requirements.txt', 'r') as file:
            #read the lines from the file
            lines = file.readlines()
            #Process each line
            for line in lines:
                #strip whitespaces and newline characters
                requirement = line.strip()
                #ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

print(get_requirements())
setup(
    name = 'AI_Trip_Planner',
    version = '0.0.1',
    author = 'Vedant Gupta',
    packages = find_packages(),
    install_requires = get_requirements()
)