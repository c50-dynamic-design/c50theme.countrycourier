from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='c50theme.countrycourier',
      version=version,
      description="An installable theme for Plone 3",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Eric Lemonne',
      author_email='eric@c50.be',
      url='https://svn.c50-hosting.com/themes',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['c50theme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
