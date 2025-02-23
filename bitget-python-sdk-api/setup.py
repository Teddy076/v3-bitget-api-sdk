#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup


setup(
    name='bitget-python',
    version='v1',
    packages=['bitget', 'bitget/ws', 'bitget/v2'],
    license="MIT",
    description="bitget-api-sdk",
    install_requires=['requests', 'websockets', 'pycryptodome', 'certifi', 'multiprocess'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
