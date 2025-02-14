#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup


setup(
    name='bitget-python',
    version='v1',
    packages=['bitget'],
    license="MIT",
    description="bitget-api-sdk",
    install_requires=['requests', 'websockets', 'pycryptodome'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
