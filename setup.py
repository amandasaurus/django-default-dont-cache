#! /usr/bin/env python

from setuptools import setup, find_packages


setup(name="django-default-dont-cache",
      version="0.1.0",
      author="Rory McCann",
      author_email="rory@technomancy.org",
      packages=['default_dont_cache'],
      license = 'GPLv3',
      description = "Opt-in caching for Django's per-site cache",
      install_requires=[ 'django' ],
)
