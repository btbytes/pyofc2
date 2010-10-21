from setuptools import setup, find_packages
import sys, os
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.rst')).read()


version = '0.1.5'

setup(name='PyOFC2',
      version=version,
      description="Python library for Open Flash Chart 2",
      long_description=README + "\n\n" + NEWS,
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
        "anyjson>=0.1",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
