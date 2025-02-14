#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup


setup(
    name='bitget',
    version='v1',
    packages=['bitget', 'bitget/ws'],
    license="MIT",
    description="bitget-api-sdk",
    install_requires=['requests', 'websockets', 'pycryptodome'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
