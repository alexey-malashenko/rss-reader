import time
from datetime import datetime
from logger import logging_dec, parameter_log
import json

log = parameter_log()


class Rss:
    cash = []
    cash_json = []

    def __init__(self, response, config):
        self.response = response
        self.config = config
        self.limit = self.get_limit()
        self.parse_response()

    @logging_dec
    def get_limit(self):
        if self.config['limit']:
            log.info('Got limit: {}'.format(self.config['limit']))
            return self.config['limit']
        else:
            limit = len(self.response['entries'])
            log.info('Got limit: {}'.format(limit))
            return limit

    @logging_dec
    def parse_response(self):

        for x in range(self.limit):

            feed = self.response['feed']['title']
            title = self.response['entries'][x]['title']

            date = str

            try:
                if self.response['entries'][x]['published_parsed']:
                    date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", self.response['entries'][x]['published_parsed'])
            except KeyError:
                date = self.config['datetime']

            link = self.response['entries'][x]['link']

            links = []

            try:
                num = 1
                for y in self.response['entries'][x]['media_content']:
                    if num == 1:
                        links.append(f'[{num}]: {self.response["entries"][x]["link"]} (link)')
                    else:
                        links.append(f'[{num}]: {y["url"]} (image)')
                    num += 1
            except KeyError:
                links.append(f'[1]: {self.response["entries"][x]["link"]} (link)')

            publish_date = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S +0000').date().__format__('%Y%m%d')

            self.cash.append({publish_date: {'Feed': feed, 'Title': title, 'Date': date, 'Link': link, 'Links': links}})
            self.cash_json = json.dumps(self.cash)

    @logging_dec
    def print_rss(self):
        if self.config['json']:
            parsed = json.loads(self.cash_json)
            print(json.dumps(parsed, indent=4, sort_keys=True))
        else:
            for rss in self.cash:
                for key, value in rss.items():
                    for k, v in value.items():
                        print(k, v)
                        print(type(v))
