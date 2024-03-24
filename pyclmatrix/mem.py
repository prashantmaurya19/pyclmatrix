from typing import Self, Tuple
from numpy import ndarray,int32,float32
from pyopencl import Buffer,mem_flags,fsvm_empty_like,fsvm_empty,SVM
from ._globals import PYCL_GLOBAL

class BufferMatrix:
    @classmethod
    def from_capacity(cls,size:int,flag:mem_flags)->Self:
        # TODO: initialize Buffer with zero
        return cls(Buffer(PYCL_GLOBAL.get_kind(None,"context"),flag,size=size))

    @classmethod
    def from_ndarray(cls,arr:ndarray,flag:mem_flags)->Self:
        return cls(Buffer(PYCL_GLOBAL.get_kind(None,"context"),flag,host_buf=arr))

    def __init__(self,matrix:Buffer) -> None:
        self.buffer = matrix

    def as_mem(self)->Buffer:
        return self.buffer

class SvmMatrix:
    @classmethod
    def from_capacity(cls,shape:Tuple[int],dtype:int32|float32)->Self:
        # TODO: initialize Buffer with zero
        return cls(fsvm_empty(PYCL_GLOBAL.get_kind(None,"context"),shape,dtype))

    @classmethod
    def from_ndarray(cls,arr:ndarray)->Self:
        return cls(fsvm_empty_like(PYCL_GLOBAL.get_kind(None,"context"),arr))

    def __init__(self,buf:ndarray) -> None:
        """
        buf is a numpy.ndarray whose numpy.ndarray.base attribute is a pyopencl.SVMAllocation.
        """
        self.buffer:ndarray = buf
        self.pointer:SVM = SVM(self.buffer)

    def as_mem(self)->SVM:
        return self.pointer



