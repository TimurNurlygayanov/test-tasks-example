# -*- coding: utf-8 -*-

import time
import requests


headers = {'Authorization': 'Bearer xoxp-<your long token here>'}
url_list = 'https://slack.com/api/channels.list'
url_list_next = 'https://slack.com/api/channels.list?cursor={0}'
url_archive = 'https://slack.com/api/conversations.archive?channel={0}&pretty=1'
url_post_message = 'https://slack.com/api/chat.postMessage'
url_chat_history = ('https://slack.com/api/conversations.history?'
                    'channel={0}&limit=10')
ARCHIVE_ASAP = []


def list_channels_to_be_archived():
    next_cursor = ''
    channels_list = []

    while next_cursor or not channels_list:
        url = url_list

        if next_cursor:
            url = url_list_next.format(next_cursor)

        res = requests.get(url, headers=headers)
        data = res.json()
        channels_list += data['channels']

        next_cursor = data.get('response_metadata').get('next_cursor')

    result = []
    for channel in channels_list:
        purpose = channel['purpose']['value']
        topic = channel['topic']['value']
        is_not_active = is_channel_not_active(channel['id'])
        if (channel['num_members'] < 2 or is_not_active) \
                and not channel['is_archived'] \
                and 'do-not-archive' not in purpose \
                and 'do-not-archive' not in topic:
            print('{0} {1}'.format(channel['id'], channel['name']))
            result.append(channel['id'])

        if 'archive-asap' in purpose or 'archive-asap' in topic:
            ARCHIVE_ASAP.append(channel['id'])

    return result


def archive_channel(channel_id):
    """ This function helps to archive the Slack channel. """

    requests.post(url_archive.format(channel_id), headers=headers)


def is_channel_not_active(channel_id):
    """ This method allows to find the channels where we didn't
        have any messages for last 60 days.
    """

    res = requests.get(url_chat_history.format(channel_id),
                       headers=headers)
    messages = res.json().get('messages', []) or []

    now = time.time()
    result = 0
    for msg in messages:
        last_date = float(msg['ts'])
        text = msg['text']

        if 'ATTENTION!!!' not in text:
            result = (now - last_date) / (3600*24)
            break

    return result > 60


def post_message(channel_id):
    """ This method allows to send messages to the Slack channel. """

    body = {
        'channel': channel_id,
        'text': ('*ATTENTION!!!* \n\n'
                 'Dear colleagues, we are going to archive this channel,'
                 ' because there are no people who are using it.\n\n'
                 )
    }
    requests.post(url_post_message, json=body, headers=headers)


# Get the list of channels which can be archived:
all_channels = list_channels_to_be_archived()

# Post message about the archiving to each selected channel:
for channel in all_channels:
    post_message(channel)

print('ASAP archive: {0}'.format(ARCHIVE_ASAP))

# Archive all channels with "archive-asap" text:
for channel in ARCHIVE_ASAP:
    post_message(channel)
    archive_channel(channel)
