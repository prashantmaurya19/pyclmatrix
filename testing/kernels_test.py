from .setup import utils,get_clplatform_info

platforms = utils.get_platform_name_space()[0]

state = get_clplatform_info(platforms)

print(state['programs'])


