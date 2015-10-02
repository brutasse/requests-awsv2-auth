# coding: utf-8
from setuptools import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='requests-awsv2-auth',
    version='1.0',
    url='https://github.com/brutasse/requests-awsv2-auth',
    license='BSD',
    author=u'Bruno Renié',
    description=('AWS v2 auth support for Python-Requests.'),
    long_description=long_description,
    py_modules=('awsv2_auth',),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=(
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ),
    install_requires=(
        'requests',
    ),
)
