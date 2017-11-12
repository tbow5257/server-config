import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/reality-catalog")
from catalog import app as application
application.secret_key = 'HrGlNQUEoCS_6If9--O4__N1'
