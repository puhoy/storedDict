# storedDict

easy json file handling

made for python3, but should be python2 compatible

## installation

    pip install storedDict


## usage

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

if autocommit is set when initializing, the commit will be called automatically on each set!
    
    >>> d = storedDict.StoredDict('testfile.json', autocommit=True)