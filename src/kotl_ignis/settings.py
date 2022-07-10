import os

HOME = os.getenv("HOME", os.getenv("USERPROFILE"))
XDG_CACHE_DIR = os.getenv("XDG_CACHE_HOME", os.path.join(HOME, ".cache"))

CACHE_DIR = os.getenv("KOTL_CACHE_DIR", os.path.join(XDG_CACHE_DIR, "kotl"))

MODULE_DIR = os.path.dirname(__file__)
THEMES_DIR = os.path.join(MODULE_DIR, 'colorschemes')
