from setuptools import setup

setup(
    name='RandOrg',
    version='0.1.0',
    author="Anthony O'Brien",
    author_email='bftm@permil.org',
    packages=['randomorg'],
    url='https://github.com/asobrien/randomOrg',
    license='LICENSE.txt',
    description='A Python wrapper to the Random.Org service.',
    long_description=open('README.rst').read(),
    install_requires=[
        "numpy",
    ],
)