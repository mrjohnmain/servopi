#!/usr/bin/env python

from setuptools import setup

setup(name='servopi',
    version='0.1',
    description='Module to control Parallax Propeller Servo Controller on Raspberry Pi. Heavily based on Roy The Robot by Tusli Software LLC',
    url='https://github.com/mrjohnmain/servopi',
    author='john Main',
    author_email='john@johnmain.co.uk',
    license='MIT',
    packages=['servopi'],
    install_requires=[
        'pyserial',
        ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        ],
    )
