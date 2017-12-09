from setuptools import setup, find_packages
from onelya_railway_sdk.api import __version__


setup(
    name='onelya_railway_sdk',
    version=__version__,
    packages=find_packages(),

    install_requires=[
        'requests'
    ],

    license='MIT License',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)