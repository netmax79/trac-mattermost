# Copyright (c) 2015-2016 Truveris, Inc. All Rights Reserved.
# See included LICENSE file.

import json

from trac.config import Option
import pkg_resources
pkg_resources.require("requests==2.31.0")
import requests


class TracMattermostComponent(object):

    webhook_url = Option("mattermost", "webhook_url",
                         doc="Preconfigured Incoming Webhook URL")
    icon_url = Option("mattermost", "icon_url",
                      doc="Icon URL to be used in notifications")
    username = Option("mattermost", "username",
                      doc="Username displayed in notifications")
    channel = Option("mattermost", "channel",
                      doc="Channel in which notifications are displayed")

    def send_notification(self, text):
        payload = {}
        if self.icon_url:
            payload["icon_url"] = self.icon_url
        if self.username:
            payload["username"] = self.username
        if self.channel:
            payload["channel"] = self.channel

        payload["text"] = text

        headers = {"Content-type": "application/json", "Accept": "text/plain"}

        requests.post(self.webhook_url, headers=headers,
                      data=json.dumps(payload))
