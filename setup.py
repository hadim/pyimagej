from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    imagej_long_description = f.read()


setup(
    name='imagej',
    # TODO: Unify version declaration to one place.
    # https://www.python.org/dev/peps/pep-0396/#deriving
    version= '0.4.0.dev0',
    author='Curtis Rueden, Yang Liu, Leon Yang',
    author_email='ctrueden@wisc.edu',
    url='https://github.com/imagej/imagej.py',
    packages=['imagej'],
    platforms=['any'],
    description='Python wrapper for ImageJ',
    long_description=imagej_long_description,
    long_description_content_type='text/markdown',
    license='Apache 2.0',
    install_requires=['pyjnius', 'scyjava', 'imglyb']
)
