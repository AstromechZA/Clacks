import smtplib
import socket
from datetime import datetime

import click
from clacks.configuration import config

def _validate_content(ctx, param, value):
    if not value:
        raise click.BadParameter("content cannot be blank")
    return value

@click.command()
@click.argument('to_address')
@click.option('--subject', default='Clacks Message', help="The subject line.")
@click.argument('content', nargs=-1, callback=_validate_content)
def email(to_address, content, subject=''):
    """
    Send plain-text content to the given TO email address. Uses the
    configured email profile.
    """

    print "Connecting.."

    session = smtplib.SMTP(
        config.get('email.smtp_server_address'),
        int(config.get('email.smtp_server_port'))
    )

    print "Starting TLS.."

    session.ehlo()
    session.starttls()
    session.ehlo()

    print "Logging In.."

    session.login(
        config.get('email.username'),
        config.get('email.password')
    )

    print "Building Message.."

    headers = "\r\n".join([
        "from: %s" % config.get('email.from_address'),
        "subject: %s" % subject,
        "to: %s" % to_address,
        "mime-version: 1.0",
        "content-type: text/html"
    ])

    # ensure it is a list of items
    if type(content) != list:
        content = [content]

    # create a paragraph for each line
    contentlines = ["<p>%s</p>" % part for part in content]

    body = "\r\n".join([
        "<h2>%s</h2>" % subject,
        "<hr>",
        " ".join(contentlines),
        "<hr>",
        "<b>Hostname:</b> %s (%s)" % (
            socket.gethostname(),
            session.sock.getsockname()[0]
        ),
        "<br>"
        "<b>Time: </b> %s" % datetime.now().strftime("%d %B %Y %H:%M:%S")
    ])

    print "Sending Message.."

    session.sendmail(
        config.get('email.username'),
        to_address,
        headers + "\r\n\r\n" + body
    )

    print "Done."
