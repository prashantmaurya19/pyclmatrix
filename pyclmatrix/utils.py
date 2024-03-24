"""
this is has platform related utils
"""

import pyopencl as cl
from typing import List, Literal

def get_platform_name_space() -> List[str]:
    """
    it is same as pyclmatrix.utils.Platform.getPlatformNameSpace()
    """
    return Platform.getPlatformNameSpace()

class Platform:
    PLATFORMS:List[cl.Platform] = cl.get_platforms()
    
    class PlatformNotFound(Exception):
        def __init__(self, *args: object,**kwargs:dict) -> None:
            super().__init__(*args,**kwargs)

    @classmethod
    def getPlatformNameSpace(cls)->List[str]:
        if cls.PLATFORMS==None:
            return []
        return [plt.name for plt in cls.PLATFORMS]

    @classmethod
    def getPlatform(cls,name:str|Literal["auto"])->cl.Platform:
        for plt in cls.PLATFORMS:
            if name=="auto":
                return plt
            if plt.name==name:
                return plt

        raise cls.PlatformNotFound(name)

    def __init__(self):
        raise BaseException("this is a singleton class.")

