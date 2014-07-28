import click

from clacks.configuration import config

@click.command()
@click.argument('to')
@click.argument('content', nargs=-1)
def email(to, content):
    """
    Send plain-text content to the given TO email address. Uses the
    configured email profile.
    """
    print to
    print content
    print config
