from rez.utils.lint_helper import env, alias, building

name = "nuke"

version = "13.1.5"

authors = ["Foundry"]

description = (
    "Family of products centered around Nuke, a powerful node-based compositing tool."
)

variants = [
    ["platform-linux"],
    # ["platform-windows"],
]

tools = ["nuke", "nukex", "nukeassist", "nukestudio", "hiero", "hieroplayer"]

has_plugins = True

uuid = "ext.nuke"

build_requires = ["ansible"]

build_command = "ansible-playbook {root}/main.yml -e 'pkg_name={name} version={version} build_path={build_path} install_path={install_path} post_build={install}'"


def commands():

    env.PATH.prepend("{root}/app")
    env.foundry_LICENSE = "${LICENSE_FILES}/foundry_rlm.lic"
    env.FN_DISABLE_LICENSE_DIALOG = (
        3  # suppress temporary license dialog until 3 days from expiry
    )
