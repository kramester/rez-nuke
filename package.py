from rez.utils.lint_helper import env, alias, building

name = "nuke"

version = "12.2.10"

authors = ["Foundry"]

description = "Nuke 12.2v10"

variants = [["platform-linux", "arch-x86_64"]]

tools = [
    'nuke',
    'nukex',
    'nukeassist',
    'nukestudio',
    'hiero',
    'hieroplayer'
    ]

has_plugins = True

uuid = "ext.nuke"


def commands():

    env.PATH.prepend("{root}/nuke")
    env.foundry_LICENSE = "4101@10.0.2.49"
    env.FN_DISABLE_LICENSE_DIALOG = 3  # suppress temporary license dialog

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
