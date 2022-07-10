#!/usr/bin/env python3

import click
import json
import os
import subprocess

from settings import THEMES_DIR
from utils import json_to_xresources

@click.command()
@click.argument('theme', required=False)
@click.option('-l', '--list-themes', is_flag=True, help='List built-in themes.')
def kotl(theme, list_themes):
    themes = os.listdir(THEMES_DIR)
    if theme:
        theme += '.json'
        if theme in themes:
            output = json_to_xresources(theme)
            subprocess.run(['xrdb', str(output)])
        else:
            print(f'No theme named {theme} found')
            exit(1)
    elif list_themes:
        for theme in themes:
            print(os.path.splitext(theme)[0])
