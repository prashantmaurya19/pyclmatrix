from .setup import pyclmatrix as pycl

platforms = pycl.utils.get_platform_name_space()[0]

state = pycl.get_clplatform_info(platforms)


