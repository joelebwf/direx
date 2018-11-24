#!/usr/bin/env python

import os

try:
    from setuptools import setup
    from setuptools.extension import Extension
except ImportError:
    raise RuntimeError('setuptools is required')

DISTNAME = 'oblib'

INSTALL_REQUIRES = ['numpy >= 1.10.1',
                    'pandas >= 0.15.0',
                    'pytz',
                    'six',
                    ]
TESTS_REQUIRE = ['pytest']
EXTRAS_REQUIRE = {
    'test': TESTS_REQUIRE
}
EXTRAS_REQUIRE['all'] = sorted(set(sum(EXTRAS_REQUIRE.values(), [])))

setuptools_kwargs = {
    'zip_safe': False,
    'scripts': [],
    'include_package_data': True
}

# set up pvlib packages to be installed and extensions to be compiled
PACKAGES = ['oblib']

extensions = []

setup(name=DISTNAME,
      packages=PACKAGES,
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      tests_require=TESTS_REQUIRE,
      ext_modules=extensions,
**setuptools_kwargs)