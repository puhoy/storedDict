import json
import logging



class AutoVivification(dict):
    """Implementation of perl's autovivification feature.
    http://stackoverflow.com/questions/651794/whats-the-best-way-to-initialize-a-dict-of-dicts-in-python
    """

    def __init__(self, storedDict, **kwargs):
        super(AutoVivification, self).__init__(**kwargs)
        self.storedDict = storedDict

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)(self.storedDict)
            if self.storedDict.autocommit:
                self.storedDict.commit()
            return value

    def __setitem__(self, key, value):
        super(AutoVivification, self).__setitem__(key, value)
        if self.storedDict.autocommit:
            self.storedDict.commit()



class StoredDict(dict):
    def __init__(self, filename, autocommit=None, *args, **kwargs):
        self.filename = filename
        self.autocommit = autocommit
        try:
            with open(filename, 'r') as f:
                super(StoredDict,self).__init__(json.load(f))
        except ValueError as e:
            logging.error(e)
            super(StoredDict,self).__init__({})
        except FileNotFoundError as e:
            logging.info('new file')
            super(StoredDict, self).__init__({})

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            self[item] = AutoVivification(self)
            if self.autocommit:
                self.commit()
            return self[item]

    def __setitem__(self, key, value):
        super(StoredDict, self).__setitem__(key, value)
        if self.autocommit:
            print('commiting %s' % json.dumps(self))
            self.commit()

    def commit(self, indent=False):
        try:
            with open(self.filename, 'w+') as f:
                json.dump(self, f, indent=indent)
        except Exception as e:
            logging.error('error while saving: %s' % e)

