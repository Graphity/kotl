import json
import os

from .settings import CACHE_DIR, THEMES_DIR


def json_to_xresources(theme):
    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)

    theme_path = os.path.join(THEMES_DIR, theme)
    theme_name = os.path.splitext(theme)[0]
    output_path = os.path.join(CACHE_DIR, theme_name)

    if os.path.exists(output_path):
        return output_path

    with open(theme_path) as f:
        theme = json.load(f)

    with open(output_path, 'w') as f:
        fg, bg = theme['foreground'], theme['background']
        f.write(f'*.foreground:\t{fg}\n*.background:\t{bg}\n*.cursorColor:\t{fg}')
        for i, color in enumerate(theme['color']):
            f.write(f'\n*.color{i}:\t{color}')

    return output_path
