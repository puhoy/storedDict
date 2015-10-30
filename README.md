# storedDict

easy json file handling


    > python3
    
    >>> import storedDict
    >>> 
    >>> d = storedDict.StoredDict('testfile.json')                                                                                                              
    >>> 
    >>> d['first'] = 'value'
    >>> d['second']['test']['foo'] = 3  # autovivification!
    >>> d.commit(indent=2)


    > cat testfile.json 
    {
      "first": "value",
      "second": {
        "test": {
          "foo": 3
        }
      }
    }

