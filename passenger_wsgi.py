import sys, os
INTERP = os.path.join(os.environ['HOME'], 'heidiwhite.net', 'venv', 'bin', 'python3')
if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

os.environ['FLASK_DEBUG'] = 'true'

sys.path.append('astrodigineous')
from astrodigineous import app as application
