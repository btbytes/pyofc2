from setuptools import setup, find_packages
import sys, os

version = '0.1.1'

setup(name='PyOFC2',
      version=version,
      description="Python library for Open Flash Chart",
      long_description="""\
PyOFC2 is a python library to generate json data that can be consumed by Open Flash Chart to produce Flash Charts. A Demo of the Flash charts generated using this library is available at http://btbytes.github.com/pyofc2 """,
      classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='flash graphics charts json visualisation visualization internet',
      author='Pradeep Kishore Gowda',
      author_email='pradeep+pyofc2@btbytes.com',
      url='http://pradeepgowda.com/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "python-cjson>=1.0.5",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
