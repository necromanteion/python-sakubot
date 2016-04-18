def first_int(*args, default=1):
    """Parse the first integer from an iterable of string arguments."""
    
    for arg in args:
        
        try:
            return int(arg)
        except ValueError:
            continue
    
    return default


def matches(string, patterns):
    """
    Filters out objects in `patterns` that do not match with `string`.
    
    args:
        string: a str to match against `patterns`
        patterns: an iterable of objects implementing a `match` method
    
    returns:
        a list of objects in `patterns` that match `string`
    """
    
    return [obj for obj in patterns if obj.match(string)]