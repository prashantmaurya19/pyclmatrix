from typing import Literal, TypedDict
from ._kernel import DEFAULT_KERNELS,Kernels
from pyopencl import Platform,Context,CommandQueue,Program

class StateDict(TypedDict):
    platform:Platform
    context:Context
    queue:CommandQueue
    programs:Kernels

class GlobalPyCL:
    class PlatformNotExists(Exception):
        def __init__(self, *args: str) -> None:
            super().__init__(*args)

    def __init__(self) -> None:
        self.state:dict[str,StateDict] = {}
        self.__current_selected_platform:str = "" 

    def set_currect_platform(self,platform:str):
        if platform not in self:
            raise self.PlatformNotExists(platform)
        self.__current_selected_platform = platform

    def get_currect_platform(self)->str:
        return self.__current_selected_platform

    def set(self,platform:Platform):
        if platform.name in self:
            return
        context = Context(devices=platform.get_devices())
        self.state[platform.name] = {
            "platform":platform,
            "context":context,
            "queue":CommandQueue(context),
            "programs":Kernels([Program(context,DEFAULT_KERNELS).build()])
        }

    def get(self,platform_name:str)->StateDict:
        if platform_name not in self:
            raise self.PlatformNotExists(platform_name)
        return self.state[platform_name]

    def get_kind(self,platform_name:str|None,kind:Literal["platform","context","queue","programs"]
                 )->Platform|Context|CommandQueue|Kernels:
        return self.get(self.get_currect_platform() if platform_name==None else platform_name)[kind]

    def __contains__(self,platform_name:str):
        return platform_name in self.state

    def __len__(self):
        return len(self.state)

        
        



