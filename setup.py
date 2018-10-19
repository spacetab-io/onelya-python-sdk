from setuptools import setup, find_packages

__version__ = '1.3.8'

setup(
    version=__version__,
    name='onelya_sdk',
    packages=find_packages(),

    install_requires=[
        'requests'
    ],

    description='Onelya Python SDK',

    author='Travel Managment Consulting',
    author_email='otd@tm-consulting.ru',

    url='https://github.com/tmconsulting/onelya-python-sdk',
    download_url='https://github.com/tmconsulting/onelya-python-sdk/archive/%s.tar.gz' % __version__,

    license='MIT License',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
