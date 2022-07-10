#!/usr/bin/env python3

import click
import json
import os
import subprocess

from .settings import THEMES_DIR, HOME
from .utils import json_to_xresources

@click.command()
@click.argument('theme', required=False)
@click.option('-l', '--list-themes', is_flag=True, help='List built-in themes.')
@click.option('--reverse', is_flag=True, help='Reverse changes.')
def kotl(theme, list_themes, reverse):
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
    elif reverse:
        subprocess.run(['xrdb', '-remove'])
        xresources_paths = [
            os.path.join(HOME, '.Xresources'),
            os.path.join(HOME, '.config/x11/xresources')
        ]
        for path in xresources_paths:
            if os.path.exists(path):
                subprocess.run(['xrdb', path])
