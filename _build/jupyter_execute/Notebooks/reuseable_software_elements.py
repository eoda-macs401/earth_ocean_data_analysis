#!/usr/bin/env python
# coding: utf-8

# # Reuseable Software Elements
# 
# Scientific software can perhaps be grouped into two categories: single-use "scripts" that are used in a very specific context to do a very specific thing (e.g.~to generate a specific figure for a paper), and reuseable components which encapsulate a more generic workflow. Once you find yourself repeating the same chunks of code in many different scripts or projects, it's time to start composing reusable software elements.

# ### Modules
# 
# The basic element of reusability in python is the [module](https://docs.python.org/3/tutorial/modules.html).
# A module is a `.py` file which contains python objects which can be _imported_ by other scripts or notebooks.
# Let's illustrate how modules work with a simple example.
# 
# A common task in geoscience is to calculate the [great-circle distance](https://en.wikipedia.org/wiki/Great-circle_distance) between two points on the globe.
# There are several [pacakges](https://pypi.python.org/pypi/geopy) that could do this for you, but let's write our own as an example of a module.
# 
# The formula for great circle distance is
# 
# ![great circle distance formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/75af53b063ee43aed3de186b1a98af5c150185b8)
# 
# (Note that this formula requires 64-bit precision for adequate accuracy.)
# 
# Let's write a module to do this calculation. Open a file called `gcdistance.py` in a text editor. (The file should be in the same directory as the notebook you are working in now.) Populate it with the following code:
# 
# ```python
# """
# A python module for computing great circle distance
# """
# import numpy as np
# 
# # approximate radius of Earth
# R = 6.371e6
# 
# def great_circle_distance(point1, point2):
#     """Calculate great-circle distance between two points.
#     
#     PARAMETERS
#     ----------
#     point1 : tuple
#         A (lat, lon) pair of coordinates in degrees
#     point2 : tuple
#         A (lat, lon) pair of coordinates in degrees
#         
#     RETURNS
#     -------
#     distance : float
#     """
#     
#     # unpack coordinates
#     lat1, lon1 = point1
#     lat2, lon2 = point2
#     
#     # unpack and convert everything to radians
#     phi1, lambda1, phi2, lambda2 = [np.deg2rad(v) for v in 
#                                     (point1 + point2)]
#     
#     # apply formula
#     # https://en.wikipedia.org/wiki/Great-circle_distance
#     return R*np.arccos(
#         np.sin(phi1)*np.sin(phi2) + 
#         np.cos(phi1)*np.cos(phi2)*np.cos(lambda2 - lambda1))
# ```
# 
# The module begins with a [docstring](https://www.python.org/dev/peps/pep-0257/) explaining what it does. Then it contains some data (just a constant `R`) and a single function.
# 
# Now let's import our module

# In[1]:


import gcdistance
help(gcdistance) 


# And let's try using it to make a calculation

# In[2]:


gcdistance.great_circle_distance((60, 0), (50, 15))


# We could just import the function we need

# In[3]:


from gcdistance import R, great_circle_distance
R


# If we change the module, we need to either restart our kernel or else reload the module. (Note that functions imported via `from module import func` cannot be reloaded.)

# In[4]:


from importlib import reload
reload(gcdistance) 


# Modules are a simple way to share code between different scripts or notebooks in the same project. _Module files must reside in the same directory as any script which imports them!_ This is a big limitation; it means you can't share modules between different projects.
# 
# Once you have a piece of code that is general-purpose enough to share between projects, you need to create a package.

# ### Aside: Python Style
# 
# There are few absolute rules for python code style, but there is a detailed [recommended style guide](https://www.python.org/dev/peps/pep-0008/). Some especially relevant points are:
# 
# * Line length should not exceed 79 characters
# * Module names should be `lowercase`
# * Function and variable names should be `lower_case_with_underscores`
# * Class names should be `CamelCase`

# ### Packages
# 
# [Packages](https://docs.python.org/3/tutorial/modules.html#packages) are python's way of encapsulating reusable code elements for sharing with others. Packaging is a huge and complicated topic. We will just scratch the surface.
# 
# We have already interacted with many packages already. Browse some of their github repositories to explore the structure of a large python package:
# 
# * NumPy: <https://github.com/numpy/numpy>
# * Pandas: <https://github.com/pandas-dev/pandas>
# * Xarray: <https://github.com/pydata/xarray>
# 
# An example of a smaller, more understandable package is our group's xrft package:
# 
# * xrft: https://github.com/xgcm/xrft
# 
# These packages all have a common basic structure. Imagine we wanted to turn our great-circle distance module into a package. It would look like this.
# 
#     README.md
#     LICENSE
#     environment.yml
#     requirements.txt
#     setup.py
#     gcdistance/__init__.py
#     gcdistance/gcdistance.py
#     gcdistance/tests/__init__.py
#     gcdistancs/tests/test_gcdistance.py
#     
# The actual package is contained in the `gcdistance` subdirectory. The other files are auxilliary files which help others understand and install your package. Here is an overview of what they do
# 
# | File Name | Purpose |
# |-----------|---------|
# | `README.txt` | Explain what the package is for |
# | `LICENSE` | Defines the legal terms under which other can use the package. [Open source](https://opensource.org/licenses/category) is encouraged! |
# | `environment.yml` | A conda environment which describes the package's dependencies ([more info](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)) |
# | `requirements.txt` | A file which describes the package's dependences for pip. ([more info](https://pip.pypa.io/en/stable/user_guide/#requirements-files))|
# | `setup.py` | A special python script which installs your package. ([more info](https://pythonhosted.org/an_example_pypi_project/setuptools.html)) |
# 

# ### The actual package
# 
# The directory `gcdistance` is the actual package. Any directory that contains an `__init__.py` file is recognized by python as a package. This file can be blank, bu it needs to be present. From the root directory, we can import a module from the package as follows
# 
# ```python
# from gcdistance import gcdistance
# ```
# 
# Yes, this is a bit redundant. That's because the `gcdistance.py` module has the same name as the `gcdistance` package directory.
# 
# However, this import will only work from the parent directory. It is not globally accessible from your python environment.

# `setup.py` is the magic file that makes your package installable and accessible anywhere. Here is an extremely basic `setup.py`
# 
# ```python
# from setuptools import setup
# 
# setup(
#     name = "gcdistance",
#     version = "0.1.0",
#     author = "Ryan Abernathey",
#     packages=['gcdistance'],
#     install_requires=['numpy'],
# )
# ```
# 
# There is a dizzying range of [options](https://setuptools.readthedocs.io/en/latest/setuptools.html) for `setup.py`. More fields are required if you want to [upload your package](https://pythonhosted.org/an_example_pypi_project/setuptools.html) to pypi (so it is installable via `pip`).
# 
# To run the setup script, we call the following from the command line
# 
#     python setup.py install
#     
# The package files are copied to our python library directory.
# If we plan to keep developing the package, we can install it in "developer mode" as
# 
#     python setup.py develop
# 
# In this case, the files are symlinked rather than copied.

# ## Testing
# 
# A software package requires [tests](https://en.wikipedia.org/wiki/Software_testing) to ensure that it works properly. Matt Rocklin has a great [blog post](http://matthewrocklin.com/blog/work/2016/02/08/tests) on why we should write tests for our code.
# 
# Tests don't have to be complicated. They are simply a check to verify that your code does what it is supposed to do.
# 
# To add tests to our project, we create create the file `gcdistance/tests/test_gcdistance.py`. (We also need an `__init__.py` file in the `tests` directory.) The example below shows an example of a test function for our package.
# 
# ```python
# import numpy as np
# import pytest
# 
# from gcdistance.gcdistance import great_circle_distance
# 
# def test_great_circle_distance():
#     # some known results
#     # distance between two same points should be zero
#     assert great_circle_distance((20., 30.), (20., 30.)) == 0
# 
#     # check distance between new york and london
#     new_york = 40.7128, -74.0060
#     london = 51.5074, 0.1278
#     dist_nyc_london = great_circle_distance(new_york, london)
#     
#     # very strict, doesn't actually work
#     # assert dist_nyc_london == 5.587e6
#     
#     # an approximate version of the above
#     np.testing.assert_allclose(dist_nyc_london, 5.587e6, rtol=1e-5)
# 
#     # now check that we can't pass the wrong number of arguments
#     with pytest.raises(TypeError):
#         great_circle_distance(1, 2, 3, 4)
# ```
# 
# We will use [pytest](https://docs.pytest.org/en/latest/getting-started.html) to run our tests. If you don't have pytest installed in your active python environment, take a minute to run `pip install pytest` from the command line. Now run
# 
# ```bash
# py.test -v
# ```
# 
# from the root directory of your project. You should see a notification that the tests passed. Try playing around with the tests to cause something to fail.
# 

# ### Continuous Integration with Travis CI
# 
# You can configure automatic testing of your package by integrating github with [Travis-CI](https://travis-ci.org/). Travis-CI is a free "continuous integration" service: it automatically downloads your package and runs your tests in the cloud every time you commit to your repository. The travis [getting started guide](https://docs.travis-ci.com/user/getting-started) gives a great overview of how to use the service.
# 
# For us to use travis with our project, the steps are simple:
# 
# 1. Push the repo to github (repo must be public)
# 1. Log in to <https://travis-ci.org> and click the switch to enable your repo
# 1. Add a `.travis.yml` file to your project with the following contents:
# 
#         language: python
#         python:
#         - 3.6
#         script:
#         - pytest
# 1. Add the file, commit, and push to github
# 1. Go to <https://travis-ci.org> and watch the magic happen!
# 
