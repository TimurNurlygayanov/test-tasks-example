# This code requires the library https://pypi.org/project/notifiers/
#

from notifiers import get_notifier


def send_feedback(text):
    p = get_notifier('slack')
    p.notify(webhook_url='https://hooks.slack.com/services/<secret_tocken>',
             message=text)
