import sys

DEBUG = False

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

try:
    if 'test' in sys.argv:
        from test_config import *
    else:
        from local_config import *
except ImportError:
    pass
