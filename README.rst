=======
RandOrg
=======

A Python Interface to the `Random.org <http://www.random.org>`_ web service. 
Provides a python wrapper to the following Random.org API calls:

- INTEGERS
- SEQUENCE
- STRING
- QUOTA

See below for usage examples.


DEPENDENCIES
------------
* Numpy

This is known to work using IPython (v0.13) and Python (2.7.3).


INSTALLATION
------------
Install with pip by running:

	pip install randorg
	
See below for usage examples.


USAGE EXAMPLES
--------------

The package can be used as follows:

.. code:: python
	
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

