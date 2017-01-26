#wsgi.py

import os, sys
apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append(project)

sys.path.append('/home/superrole/Documents/python/cpr_equipment')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cpr_equipment.apache.override'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
