from typing import Literal
# from colori import colori as clr
# import pyopencl as pcl
from pyclmatrix import utils


#don't touch this variable
PYCL_GLOBAL:dict = {}

def is_initialized()->bool:
    global PYCL_GLOBAL
    return 0 < len(PYCL_GLOBAL)


def init(platform_name:str|Literal["auto"]="auto",device_id:int=0):
    """
    platform_name : is name of platform which can find by pyclmatrix.utils.Platfrom.getPlatformNameSpace(). if it auto then it will automaticly select a platform

    device_id : index of your gpu in platfrom devices array
    """



