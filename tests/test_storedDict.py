import unittest
import json
import os
from storedDict import StoredDict


class TestStoredDict(unittest.TestCase):

    def test_save_and_load(self):
        val = 1
        sd = StoredDict('testing.json')
        sd['one'] = val
        sd.commit()
        sd = StoredDict('testing.json')
        self.assertEqual(val, sd['one'])
        val2 = 2
        sd['two'] = 2
        sd.commit()
        self.assertEqual(val, sd['one'])
        self.assertEqual(val2, sd['two'])

    def test_autovivification(self):
        sd = StoredDict('testing.json')
        sd['one']['two']['three'] = 3
        val = sd['one']['two']['three']
        sd.commit()
        with open('testing.json', 'r') as f:
            loaded_sd = json.load(f)
        self.assertEqual(val, loaded_sd['one']['two']['three'])

    def test_autocommit(self):
        sd = StoredDict('testing.json', autocommit=True)
        sd['one'] = 3
        val = sd['one']
        # no manual commit here
        with open('testing.json', 'r') as f:
            loaded_sd = json.load(f)
        self.assertEqual(sd['one'], loaded_sd['one'])

    def test_autoviv_autocommit(self):
        sd = StoredDict('testing.json', autocommit=True)
        sd['one']['two']['three'] = 3
        val = sd['one']['two']['three']
        # no manual commit here
        with open('testing.json', 'r') as f:
            loaded_sd = json.load(f)
        self.assertEqual(val, loaded_sd['one']['two']['three'])

    def test_load_saved_dict(self):
        sd2 = StoredDict('tests/testing2.json')
        sd2.commit()
        self.assertEqual(3, sd2['one']['two']['three'])

    def tearDown(self):
        try:
            os.remove('testing.json')
            pass
        except:
            pass

if __name__ == '__main__':
    unittest.main()