# HTTP GET to interact with Random.org

import urllib
import urllib2
import os.path
import numpy as np

# CONFIG
RANDOM_URL = 'http://www.random.org'


def integers(num, minimum, maximum, base=10):
    # TODO: Ensure numbers within bounds
    """Docstring."""
    FUNC_TYPE = 'integers'
    
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
    
    url_opts = urllib.urlencode(opts)
    full_url = os.path.join(RANDOM_URL, FUNC_TYPE) + '/?' + url_opts
    data = urllib2.urlopen(full_url)
    if data.code == 200: 
        # Status is Good
        arr = np.fromstring(data.read(), sep='\n', dtype='int')
    else:
        print "random.org returned server code: %s" % data.code
    return arr




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


    
    
    
    
    
    
    
    
    
    
    


# 
# 
# #################################
# ####### START OF PROGRAM ########
# #################################
# 
# quotaCheck = urllib.urlopen('http://www.random.org/quota/?format=plain').read()  # Check to see if you have bits remaining on the server
# 
# if quotaCheck > 0:
#     getString='http://www.random.org/integers/?num=25&min=0&max=16&col=1&base=16&format=plain&rnd=new'
#     randomData = urllib.urlopen(getString).read()
#     print(randomData)
#     print 
#     print 'You have', quotaCheck.strip(), 'bits remaining on the server.'
#     
# else:
#     print 'You have no remaing requests on the Random.org server; wait at least 10 minutes before making another request. It may take 24 hours for you to gain access the server again.'
#     
# 
# sitePath = 'http://www.random.org/'
# 
# # Integer sequence from random.org
# def randInt(num, min, max, base=10, format='plain', columns=1, dataType='new'):
#     appPath = 'integers/?'
#     params = ['num', str(num),
#               'min', str(min),
#               'max', str(max), 
#               'base', str(base), 
#               'format', format,
#               'col', str(columns),
#               'rnd', dataType]
#     
#     for i in range(1, len(params) + len(params)/2, 3):
#         params.insert(i, '=')
#     
#     for i in range(3, len(params) + (len(params)/3-1), 4):
#         params.insert(i, '&')
#         
#     
#     params = "".join(params)    
#     getString = sitePath + appPath + params
#     randomData = urllib.urlopen(getString).read()
#     print(getString)
#     print(randomData)
#     return randomData
#     # TODO: learn more about "return" in a function
# 
# 
# # TODO: create a function that simulates tossing a coin by calling on randInt(tosses, min=0, max=1), where HEADS is sum/tosses >= 0.5.
# 
# # def coinToss(tosses=100):
#     # randInt(tosses, 0, 1)
