from typing import Any, List
from pyopencl import Program,kernel_info
from .mem import SvmMatrix,BufferMatrix
from functools import partial


DEFAULT_KERNELS: str = """
kernel void scaler_mutiply(){
}
kernel void matix_mutiply(){
}
"""

class Kernels:
    class KernelNotFound(Exception):
        def __init__(self, *args: str,**kwargs:object) -> None:
            super().__init__(*args,**kwargs)

    def __init__(self,progs:List[Program]=[]):
        self.state:dict[str,int] = {}
        self.programs:List[Program] = []
        self.register_programs(progs)
    
    @classmethod
    def get_kernel_names_from_program(cls,prog:Program)->List[str]:
        return [ k.get_info(kernel_info.FUNCTION_NAME) for k in prog.all_kernels()]

    @classmethod
    def preprocess_args_list(cls,*args:SvmMatrix|BufferMatrix)->List:
        return [k.as_mem() for k in args]

    def __set_kernel_state(self,kernel_name:str,index:int):
        self.state[kernel_name] = index

    def __kernel_func(self,kernel_name:str,*args:SvmMatrix|BufferMatrix,**kwargs:object):
        # print(kernel_name,args,kwargs)
        getattr(self.get_kernel(kernel_name),kernel_name)(*self.preprocess_args_list(*args),**kwargs)

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

    def __getattribute__(self,name:str)->Any:
        try:
            return super().__getattribute__(name)
        except:
            if name not in self:
                raise self.KernelNotFound(name)
            return partial(self.__kernel_func,name)

    def __getitem__(self,name:str)->Program:
        return self.get_kernel(name)

    def __len__(self):
        return len(self.state)

