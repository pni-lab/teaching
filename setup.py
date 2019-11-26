#!/usr/bin/env python

from setuptools import setup, find_packages
#import versioneer

setup(name='teaching-pni',
      version=0.0,  #versioneer.get_version(),
      # cmdclass=versioneer.get_cmdclass(),
      description='Teaching material (alpha version)',
      author='Tamas Spisak',
      author_email='tamas.spisak@uk-essen.de,',
      packages=find_packages('teaching-pni'),
      scripts=['bin/boostit.py', 'bin/boostit-spark.sh'], install_requires=['numpy', 'pandas', 'plotly', 'scikitlearn']
      )