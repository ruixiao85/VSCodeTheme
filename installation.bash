conda create -c conda-forge -n node nodejs
conda activate node

npm install -g vsce

# make edits to themes and update package version
vsce package

# https://ruixiao85.visualstudio.com/ look for settings/personal token

vsce publish
