import click
from twitter import *

from clacks.configuration import config

@click.command()
@click.argument('content')
def tweet(content):
    """
    Tweet the given content
    """
    t = Twitter(auth=(
        config['twitter.oauth_token'],
        config['twitter.oauth_secret'],
        config['twitter.consumer_key'],
        config['twitter.consumer_secret'],
    ))

    content = " ".join(content)

    if len(content) > 140:
        content = content[:-3] + '...'

    t.statuses.update(status=content)
