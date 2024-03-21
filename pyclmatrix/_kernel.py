from typing import List
from pyopencl import Program,kernel_info


"""default kernels"""
DEFAULT_KERNELS: str = """
kernel void scaler_mutiply(){
}
kernel void matix_mutiply(){
}
"""

class Kernels:
    class KernelNotFound(Exception):
        def __init__(self, *args: object,**kwargs:dict) -> None:
            super().__init__(*args,**kwargs)

    def __init__(self,progs:List[Program]=[]):
        self.state:dict[str,int] = {}
        self.programs:List[Program] = []
        self.register_programs(progs)
    
    @classmethod
    def get_kernel_names_from_program(cls,prog:Program)->List[str]:
        return [ k.get_info(kernel_info.FUNCTION_NAME) for k in prog.all_kernels()]

    def __set_kernel_state(self,kernel_name:str,index:int):
        self.state[kernel_name] = index

    def register_programs(self,progs:List[Program]):
        for p in progs:
            self.add_program(p)

    def add_program(self,prog:Program):
        prog_index = len(self.programs)
        self.programs.append(prog)
        for kname in self.get_kernel_names_from_program(prog):
            self.__set_kernel_state(kname, prog_index)

    def get_kernel(self,name:str)->Program:
        if name not in self:
            raise self.KernelNotFound("name")
        return self.programs[self.state[name]]

    def __str__(self)->str:
        res = f"Kernels{[f"{k}:{self.state[k]}" for k in self.state]}"
        return res

    def __contains__(self,name:str)->bool:
        return name in self.state

    def __getattr__(self,name:str)->Program:
        return self[name]

    def __getitem__(self,name:str)->Program:
        return self.get_kernel(name)

    def __len__(self):
        return len(self.state)

