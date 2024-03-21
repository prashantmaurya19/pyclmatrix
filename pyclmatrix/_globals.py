from typing import TypedDict
from ._kernel import DEFAULT_KERNELS,Kernels
from pyopencl import Platform,Context, device_type,CommandQueue,Program

class StateDict(TypedDict):
    platform:Platform
    context:Context
    queue:CommandQueue
    programs:Kernels

class GlobalPyCL:

    class PlatformNotExists(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)

    def __init__(self) -> None:
        self.state:dict[str,StateDict] = {}

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

    def __contains__(self,platform_name:str):
        return platform_name in self.state

    def __len__(self):
        return len(self.state)

        
        



