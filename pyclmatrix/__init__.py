from typing import Literal
from pyopencl import Context, Platform
from .utils import Platform as platform
from ._globals import StateDict,PYCL_GLOBAL
from ._kernel import Kernels

def is_initialized()->bool:
    global PYCL_GLOBAL
    return 0 < len(PYCL_GLOBAL)

def is_platform_itialized(platform_name:str)->bool:
    global PYCL_GLOBAL
    return platform_name in PYCL_GLOBAL

def init(platform_name:str|Literal["auto"]="auto"):
    """platform_name:
        is name of platform which can find by pyclmatrix.utils.get_platform_name_space(). if it auto then it will automaticly select a platform
    """
    global PYCL_GLOBAL
    if is_initialized():
        return
    PYCL_GLOBAL.set(platform.getPlatform(platform_name))

def get_clplatform_info(platform_name:str)->StateDict:
    return PYCL_GLOBAL.get(platform_name)

def get_platform(platform_name:str|None=None)->Platform:
    global PYCL_GLOBAL
    return PYCL_GLOBAL.get_kind(platform_name,"platform")

def get_context(platform_name:str|None=None)->Context:
    global PYCL_GLOBAL
    return PYCL_GLOBAL.get_kind(platform_name,"context")

def get_kernel(platform_name:str|None=None)->Kernels:
    global PYCL_GLOBAL
    return PYCL_GLOBAL.get_kind(platform_name,"programs")

def get_command_queue(platform_name:str|None=None)->Kernels:
    global PYCL_GLOBAL
    return PYCL_GLOBAL.get_kind(platform_name,"queue")
