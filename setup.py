from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='cisco-prime',
    version=version,
    description="Basic Cisco prime web client",
    keywords='Cisco prime',
    author='Justin Azoff',
    author_email='JAzoff@albany.edu',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    zip_safe=False,
    install_requires=[
        "requests",
    ],
)
