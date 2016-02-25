# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import os


version = '1.0.4'
description = 'Hooks to facilitate managing custom index values in Zope 2/CMF applications'  # noqa
long_description = ('\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.rst').read(),
    open(os.path.join("plone", "indexer", "README.rst")).read(),

]))


setup(
    name='plone.indexer',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Zope2",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='plone cmf zope catalog index',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/plone.indexer',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.interface',
        'zope.component',
        'Products.CMFCore',
        'Products.ZCatalog',
    ],
)
