"""
this is has platform related utils
"""

import pyopencl as pyc
from typing import List

class Platfrom:
    PLATFORMS:List[pyc.Platform] = pyc.get_platforms()
    
    class PlatformNotFound(Exception):
        def __init__(self, *args: List,**kwargs:dict) -> None:
            super().__init__(*args,**kwargs)

    @classmethod
    def getPlatformNameSpace(cls)->List[str]:
        if cls.PLATFORMS==None:
            return []
        return [plt.name for plt in cls.PLATFORMS]

    @classmethod
    def getPlaform(cls,name:str)->pyc.Platform:
        for plt in cls.PLATFORMS:
            if plt.name==name:
                return plt

        raise cls.PlatformNotFound(f"platform : {name}")

    
    def __init__(self):
        raise BaseException("this is a singleton class.")




