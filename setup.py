from setuptools import find_packages,setup
from typing import List

"""
The -e . in requirements.txt connects setup.py and runs it simultanesously
but along with packages specified even -e . comes so we have to remove that
"""
HYPEN_E_DOT='-e .' ## Constant for hypen e dot 

def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        for line in file_obj:
            req=line.strip()
            if req and req!= HYPEN_E_DOT:
                requirements.append(req)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Bhumika Shankar',
author_email='bhumikshankar2003@gmail.com',
packages=find_packages(),
install_requires=get_requirements('dev-requirements.txt')


)