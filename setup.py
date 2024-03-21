import shutil,os
from setuptools import setup,find_packages
name = "pyclmatrix"
version = "0.0.1"

def deleteIfExists(path:str):
    """
        path:- relative path of directory.

        deletes the folder if it exists.
    """
    path = os.path.join(os.getcwd(),path)
    if os.path.exists(path):
        shutil.rmtree(path)

deleteIfExists('build')
deleteIfExists('dist')
deleteIfExists(f'{name}.egg-info')

setup(
    version=version,
    name=name,
    packages=find_packages(),
    requires=[]
)
