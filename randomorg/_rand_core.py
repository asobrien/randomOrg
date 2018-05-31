from __future__ import absolute_import, print_function

# CORE UTILITIES TO CREATE HTTP GET REQUESTS TO INTERACT WITH RANDOM.ORG
import sys
# if python version below 3
if sys.version_info < (3,):
    from urllib2 import urlopen
    from urllib import urlencode
else:
    from urllib.request import urlopen
    from urllib.parse import urlencode

import os.path
import numpy as np

### CONFIG ###
RANDOM_URL = 'http://www.random.org'
### END CONFIG ###


### MAIN FUNCTIONS ###

def integers(num, minimum, maximum, base=10):
    # TODO: Ensure numbers within bounds
    """Random integers within specified interval.
    
    The integer generator generates truly random integers in the specified 
    interval. 
                        
    Parameters
    ----------
    num : int, bounds=[1, 1E4]
          Total number of integers in returned array.
    minimum : int, bounds=[-1E9, 1E9]
              Minimum value (inclusive) of returned integers.
    maximum : int, bounds=[-1E9, 1E9]
              Maximum value (inclusive) of returned integers.
    base: int, values=[2, 8, 10, 16], default=10
          Base used to print numbers in array, the default is decimal 
          representation (base=10).
    
    Returns
    -------
    integers : array
               A 1D numpy array containing integers between the specified
               bounds.
    
    Examples
    --------
    Generate an array of 10 integers with values between -100 and 100, 
    inclusive:
    
    >>> integers(10, -100, 100)

    A coin toss, where heads=1 and tails=0, with multiple flips (flips should 
    be an odd number):

    >>> sum(integers(5, 0, 1))

    """
    function = 'integers'

    num, minimum, maximum = list(map(int, [num, minimum, maximum]))

    # INPUT ERROR CHECKING
    # Check input values are within range
    if (1 <= num <= 10 ** 4) is False:
        print('ERROR: %s is out of range' % num)
        return
    if (-10 ** 9 <= minimum <= 10 ** 9) is False:
        print('ERROR: %s is out of range' % minimum)
        return
    if (-10 ** 9 <= maximum <= 10 ** 9) is False:
        print('ERROR: %s is out of range' % maximum)
        return
    if (maximum < minimum):
        print('ERROR: %s is less than %s' % (maximum, minimum))
        return

    base = int(base)
    if base not in [2, 8, 10, 16]:
        raise Exception('Base not in range!')

    opts = {'num': num,
            'min': minimum,
            'max': maximum,
            'col': 1,
            'base': base,
            'format': 'plain',
            'rnd': 'new'}
    integers = get_http(RANDOM_URL, function, opts)
    integers_arr = str_to_arr(integers)
    return integers_arr


def sequence(minimum, maximum):
    """Randomize a sequence of integers."""
    function = 'sequences'
    opts = {'min': minimum,
            'max': maximum,
            'col': 1,
            'format': 'plain',
            'rnd': 'new'}
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

    opts = {'num': num,
            'len': length,
            'digits': digits,
            'upperalpha': upper,
            'loweralpha': lower,
            'format': 'plain',
            'rnd': 'new'}
    seq = get_http(RANDOM_URL, function, opts)
    seq = seq.strip().split('\n')  # convert to list
    # seq_arr = str_to_arr(seq)  # 
    return seq


def quota(ip=None):
    """Check your quota."""
    # TODO: Add arbitrary user defined IP check
    url = 'http://www.random.org/quota/?format=plain'
    data = urlopen(url)
    credit = int(data.read().strip())
    if data.code == 200:
        return credit
    else:
        return "ERROR: Server responded with code %s" % data.code


### HELPER FUNCTIONS ###

def get_http(base_url, function, opts):
    """HTTP request generator."""
    url = (os.path.join(base_url, function) + '/?' + urlencode(opts))
    data = urlopen(url)

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
