#!/bin/bash

# TODO Add your required rpm packages here
pkgs+=(python3)
source "${TOOLBOX_PROFILE_PATH}/toolbox.common.sh"

toolbox_helper_install_vscode
toolbox_helper_pip_install

toolbox enter "${TOOLBOX}" <<EOF
git submodule init
git submodule update
exit
EOF
