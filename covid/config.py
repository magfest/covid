from sideboard.lib import parse_config

from uber.config import c, Config
from uber.menu import MenuItem

config = parse_config(__file__)
c.include_plugin_config(config)