from .setup import utils,get_kernel


platforms = utils.get_platform_name_space()[0]
state = get_kernel(platforms)

print(state)


