import unittest
import json
import os

from storedDict import StoredDict


class TestStoredDict(unittest.TestCase):

    def test_autovivification(self):
        print('autoviv')
        sd = StoredDict('testing.json')
        sd['one']['two'] = 3
        val = sd['one']['two']
        sd.commit()
        with open('testing.json', 'r') as f:
            loaded_sd = json.load(f)
        self.assertEqual(val, loaded_sd['one']['two']) #zf

    def test_autocommit(self):
        print('autocomm')
        sd = StoredDict('testing.json', autocommit=True)
        sd['one'] = 3
        val = sd['one']
        # no manual commit here
        with open('testing.json', 'r') as f:
            loaded_sd = json.load(f)
        self.assertEqual(sd['one'], loaded_sd['one'])

    def test_autoviv_autocommit(self):
        print('autoviv_autocomm')
        sd = StoredDict('testing.json', autocommit=True)
        sd['one']['two']['three'] = 3
        val = sd['one']['two']['three']
        # no manual commit here
        with open('testing.json', 'r') as f:
            loaded_sd = json.load(f)
        self.assertEqual(val, loaded_sd['one']['two']['three'])

    def tearDown(self):
        os.remove('testing.json')