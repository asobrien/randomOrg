# CORE UTILITIES TO CREATE HTTP GET REQUESTS TO INTERACT WITH RANDOM.ORG

import urllib
import urllib2
import os.path
import numpy as np


### CONFIG ###
RANDOM_URL = 'http://www.random.org'
### END CONFIG ###



### MAIN FUNCTIONS ###

def integers(num, minimum, maximum, base=10):
    # TODO: Ensure numbers within bounds
    """Docstring."""
    function = 'integers'
    
    num, minimum, maximum = map(int, [num, minimum, maximum])
    # Attribute error ?
    
    base = int(base)
    
    if base not in [2,8,10,16]:
        raise
    
    opts = {'num':num, 
            'min':minimum, 
            'max':maximum, 
            'col':1, 
            'base':base, 
            'format':'plain',
            'rnd':'new'}
    integers = get_http(RANDOM_URL, function, opts)
    integers_arr = str_to_arr(intergers)
    return integers_arr


def sequence(minimum, maximum):
    """Randomize a sequence of integers."""
    function = 'sequences'
    opts = {'min':minimum, 
            'max':maximum, 
            'col':1, 
            'format':'plain',
            'rnd':'new'}
    deal = get_http(RANDOM_URL, function, opts)
    deal_arr = str_to_arr(deal)
    return deal_arr


def string(num, length, digits=False, upper=True, lower=True, unique=False):
    """Random strings."""
    function = 'strings'
    # Convert arguments to random.org style
    # for a discussion on the method see: http://bit.ly/TKGkOF 
    digits = convert(digits)
    upper = convert(upper)
    lower = convert(lower)
    unique = convert(unique)
    
    opts = {'num':num, 
            'len':length, 
            'digits':digits, 
            'upperalpha':upper, 
            'loweralpha':lower, 
            'format':'plain',
            'rnd':'new'}
    seq = get_http(RANDOM_URL, function, opts)
    seq = seq.strip().split('\n')  # convert to list
    # seq_arr = str_to_arr(seq)  # 
    return seq


def quota(ip=None):
    """Check your quota."""
    # TODO: Add arbitrary user defined IP check
    url = 'http://www.random.org/quota/?format=plain'
    data = urllib2.urlopen(url)
    credit = int(data.read().strip())
    if data.code == 200:
        return credit
    else:
        return "ERROR: Server responded with code %s" % data.code




### HELPER FUNCTIONS ###

def get_http(base_url, function, opts):
    """HTTP request generator."""
    url = (os.path.join(base_url, function) + '/?' +   
                 urllib.urlencode(opts))
    data = urllib2.urlopen(url)
    
    if data.code != 200:
        raise ValueError("Random.rg returned server code: " + str(data.code)) 
    return data.read()

    
def str_to_arr(string):
    """Converts string to numpy array."""
    arr = np.fromstring(string, sep='\n', dtype='int')
    return arr


def convert(self):
    # TODO: Add proper TypeError
    if self == True:
        self = 'on'
        return self
    elif self == False:
        self = 'off'
        return self
    else: 
        return "TypeERROR: not a boolean"

# EOF