from setuptools import setup, find_packages

import os
import re


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('mc2p')

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


setup(
    name='mc2p-python',
    version=version,
    url='https://github.com/mc2p/mc2p-python',
    license='BSD',
    description='MyChoice2Pay Pythoni Bindings',
    long_description=README,
    author='MyChoice2Pay',
    author_email='support@mychoice2pay.com',
    download_url='https://github.com/mc2p/mc2p-python/archive/v0.0.2.tar.gz',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    keywords=['mychoice2pay', 'payments'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
