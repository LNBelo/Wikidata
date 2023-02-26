# -*- coding: utf-8 -*-
"""
source: https://github.com/maxlath/wikibase-cli

The file to be executed can be a .js or a .json
"""

import os

# credentials
os.system("wb config credentials https://www.wikidata.org")
choice = input(str('Continue: Yes[y] or No[n]?\n'))
if choice in ['n', 'N']:
    exit()

os.system("wb edit-entity ./temp.js")

# exit
# os.system("wb config credentials https://www.wikidata.org reset")
