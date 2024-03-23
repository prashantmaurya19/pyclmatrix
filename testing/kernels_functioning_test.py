from .setup import utils,get_kernel

platforms = utils.get_platform_name_space()[0]
prog = get_kernel(platforms)
print(prog)
print(getattr(prog,"scaler_mutiply"))

