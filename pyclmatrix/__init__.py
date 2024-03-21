from typing import Literal
from .utils import Platfrom
from ._globals import GlobalPyCL,StateDict



#don't touch this variable
PYCL_GLOBAL:GlobalPyCL = GlobalPyCL()

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

    PYCL_GLOBAL.set(Platfrom.getPlatform(platform_name))

def get_clplatform_info(platform_name:str)->StateDict:
    return PYCL_GLOBAL.get(platform_name)
