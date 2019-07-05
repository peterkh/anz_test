import os
from .context import status_app

import unittest

class StatusTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_status(self):
        os.environ['APP_VERSION'] = "1.0"
        os.environ['COMMIT_SHA'] = "aaaaa"
        assert(status_app.main.status() == "{}")

if __name__ == '__main__':
    unittest.main()
