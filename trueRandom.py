# HTTP GET to interact with Random.org

import urllib

#################################
####### START OF PROGRAM ########
#################################

quotaCheck = urllib.urlopen('http://www.random.org/quota/?format=plain').read()  # Check to see if you have bits remaining on the server

if quotaCheck > 0:
	getString='http://www.random.org/integers/?num=25&min=0&max=16&col=1&base=16&format=plain&rnd=new'
	randomData = urllib.urlopen(getString).read()
	print(randomData)
	print 
	print 'You have', quotaCheck.strip(), 'bits remaining on the server.'
	
else:
	print 'You have no remaing requests on the Random.org server; wait at least 10 minutes before making another request. It may take 24 hours for you to gain access the server again.'
	

sitePath = 'http://www.random.org/'

# Integer sequence from random.org
def randInt(num, min, max, base=10, format='plain', columns=1, dataType='new'):
	appPath = 'integers/?'
	params = ['num', str(num),
			  'min', str(min),
			  'max', str(max), 
			  'base', str(base), 
			  'format', format,
			  'col', str(columns),
			  'rnd', dataType]
	
	for i in range(1, len(params) + len(params)/2, 3):
		params.insert(i, '=')
	
	for i in range(3, len(params) + (len(params)/3-1), 4):
		params.insert(i, '&')
		
	
	params = "".join(params)	
	getString = sitePath + appPath + params
	randomData = urllib.urlopen(getString).read()
	print(getString)
	print(randomData)
	return randomData
	# TODO: learn more about "return" in a function


# TODO: create a function that simulates tossing a coin by calling on randInt(tosses, min=0, max=1), where HEADS is sum/tosses >= 0.5.

# def coinToss(tosses=100):
	# randInt(tosses, 0, 1)
