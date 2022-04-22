from os.path import join

import cherrypy
import uber
from uber.errors import HTTPRedirect
from uber.jinja import template_overrides
from uber.models import Attendee, Session
from uber.utils import mount_site_sections, static_overrides

from ._version import __version__  # noqa: F401
from .config import config


# These need to come last so they can make use of config properties
from .utils import *  # noqa: F401,E402,F403
from .models import *  # noqa: F401,E402,F403
from .automated_emails import *  # noqa: F401,E402,F403
from .model_checks import *  # noqa: F401,E402,F403

# Silence pyflakes
from .models import PrevSeasonSupporter  # noqa: E402

static_overrides(join(config['module_root'], 'static'))
template_overrides(join(config['module_root'], 'templates'))
mount_site_sections(config['module_root'])