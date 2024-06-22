from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function returns list of requirements
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace('\n', "") for req in requirements]
        
    return requirements

setup(
name = 'mlproject',
version = '0.0.1',
author = 'rutik',
author_email = 'rutik20.rb@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)