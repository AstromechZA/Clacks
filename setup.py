from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='clacks',
    version='0.1',
    author='Ben Meier',
    author_email='benmeier42@gmail.com',
    license='MIT',
    description='A simple CLI for sending text notifications via email or tweet.',
    long_description=read('README.md'),
    packages=find_packages(exclude=['tests']),
    scripts=[
        'scripts/clacks_send',
        'scripts/clacks_config'
    ],
    install_requires=[
        'Click',
        'Twitter'
    ],
    test_suite='nose.collector',
    tests_require='nose',
)

# TODO: http://click.pocoo.org/setuptools/#setuptools-integration
