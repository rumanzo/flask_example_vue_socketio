import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app as application
application.debug = True

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug=True)
