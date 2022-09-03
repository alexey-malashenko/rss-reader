"""The module is intended for parsing and printing RSS"""

import time
import json
from datetime import datetime
from logger import logging_dec, parameter_log

log = parameter_log()


class Rss:
    """Define the class for RSS

        Returns:

        """

    cash = []
    cash_json = []

    def __init__(self, response, config):
        self.response = response
        self.config = config
        self.limit = self.get_limit()
        self.parse_response()

    @logging_dec
    def get_limit(self):
        """Define the limit RSS

            Returns:
                limit
            """

        if self.config['limit']:
            if self.config['limit'] <= len(self.response['entries']):
                log.info('Got limit: {}'.format(self.config['limit']))
                return self.config['limit']
            else:
                log.info('Got limit: {}'.format(len(self.response['entries'])))
                return len(self.response['entries'])
        else:
            limit = len(self.response['entries'])
            log.info('Got limit: {}'.format(limit))
            return limit

    @logging_dec
    def parse_response(self):
        """Define the structure of feeds

            Returns:

            """

        for x in range(self.limit):

            feed = self.response['feed']['title']
            log.info('Got feed: {}'.format(feed))
            title = self.response['entries'][x]['title']
            log.info('Got title: {}'.format(title))

            date = str

            try:
                if self.response['entries'][x]['published_parsed']:
                    date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", self.response['entries'][x]['published_parsed'])
            except KeyError:
                date = self.config['datetime']
            log.info('Got date: {}'.format(date))

            link = self.response['entries'][x]['link']
            log.info('Got link: {}'.format(link))

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
            log.info('Got links: {}'.format(links))

            publish_date = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S +0000').date().__format__('%Y%m%d')
            log.info('Got publish_date: {}'.format(publish_date))

            self.cash.append({publish_date: {'Feed': feed, 'Title': title, 'Date': date, 'Link': link, 'Links': links}})
            log.info('Got cash: {}'.format(self.cash))
            self.cash_json = json.dumps(self.cash)
            log.info('Got cash_json: {}'.format(self.cash_json))

    @logging_dec
    def print_rss(self):
        """Define the printing feeds

            Returns:

            """

        if self.config['json']:
            parsed = json.loads(self.cash_json)
            log.info('Got parsed: {}'.format(parsed))
            print(json.dumps(parsed, indent=4, sort_keys=True))
        else:
            for rss in self.cash:
                log.info('Got rss: {}'.format(rss))
                for key, value in rss.items():
                    print(f"\nFeed: {value.get('Feed')}\n")
                    print(f"Title: {value.get('Title')}")
                    print(f"Date: {value.get('Date')}")
                    print(f"Link: {value.get('Link')}\n")
                    print(f"Links:")
                    for link in value.get('Links'):
                        print(f"{link}")
                    print(f"\n")
