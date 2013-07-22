=========
RandomOrg
=========

A Python Interface to the `Random.org <http://www.random.org>`_ web service.


DEPENDENCIES
----------
* Numpy

This is known to work using IPython (v0.13) and Python (2.7.3).


INSTALLATION
----------
Install the egg with `easy_install` by running:

	easy_install https://github.com/downloads/asobrien/randomOrg/randorg-0.1.egg
	
You may need to run the command above using `sudo`


USAGE EXAMPLES
--------------

The package can be used as follows:

	import randomorg as ro
	
	# Generate 5 integers between 1 and 100
	ro.integers(5, minimum=1, maximum=100, base=10)
	
	# Generate a random sequence of integers between 1 and 10
	ro.sequence(minimum=1, maximum=10)
	
	# Generate 5 unique strings (e.g. passwords) of 10 characters each
	ro.string(num=5, length=10, digits=True, upper=True, 
				lower=True, unique=True)
	
	# Check your quota
	ro.quota()
	

That pretty much sums up the functions included in the random.org api. More information on the random.org api can be found `here <http://www.random.org/clients/http/>`_.


VERSION LOG
---------

### v0.1 ###
* Initial release, contains core api functions:
	- INTEGERS
	- SEQUENCE
	- STRING
    - QUOTA