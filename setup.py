from setuptools import setup
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
    packages=[
        'clacks',
    ],
    scripts=[
        'scripts/clacks_send',
        'scripts/clacks_config'
    ],
    install_requires=[
        'Click',
        'Twitter'
    ],
)

# TODO: http://click.pocoo.org/setuptools/#setuptools-integration
