import os
import sys
import unittest

# Add the app directory to the PYTHONPATH
sys.path.append('../app/controllers')
sys.path.append('../app/db')
sys.path.append('../app/service')
sys.path.append('../app/db')
import os
import sys

# Add the app directory to the Python path
app_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, app_dir)
sys.path.insert(0, os.path.join(app_dir, 'controllers'))
sys.path.insert(0, os.path.join(app_dir, 'db'))
sys.path.insert(0, os.path.join(app_dir, 'service'))
sys.path.insert(0, os.path.join(app_dir, 'db'))

# Create a test suite
test_suite = unittest.TestLoader().discover('.', pattern='*.py')

# Run the test suite
unittest.TextTestRunner().run(test_suite)