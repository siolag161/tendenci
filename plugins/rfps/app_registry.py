from registry import site
from registry.base import PluginRegistry, lazy_reverse
from rfps.models import RFP


class RFPRegistry(PluginRegistry):
    version = '1.0'
    author = 'Schipul - The Web Marketing Company'
    author_email = 'programmers@schipul.com'
    description = 'Create rfps type of content'

site.register(RFP, RFPRegistry)