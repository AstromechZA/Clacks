import click

from clacks.configuration import config

@click.command()
@click.argument('content')
def tweet(content):
    """
    """
    print 1
