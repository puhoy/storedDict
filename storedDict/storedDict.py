import json

class AutoVivification(dict):
    """Implementation of perl's autovivification feature.
    http://stackoverflow.com/questions/651794/whats-the-best-way-to-initialize-a-dict-of-dicts-in-python
    """
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

class StoredDict(dict):
    def __init__(self, filename, **kwargs):
        self.filename = filename
        try:
            super(StoredDict,self).__init__(json.load( open(filename, 'r')))
        except ValueError:
            print('value err')
            super(StoredDict,self).__init__({})
        except FileNotFoundError:
            print('file not found err')
            super(StoredDict,self).__init__({})

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = AutoVivification()
            return value

    def commit(self):
        json.dump(self, open(self.filename, 'w+'), indent=2)

