"""The module is intended for reading RSS cache"""

import json
from logger import logging_dec, parameter_log
from checker import check_cache_file


log = parameter_log()


class RssCacher:
    """Define the class for RSS cache

        Returns:

        """

    cash = []
    cash_json = []

    def __init__(self, config, path_cache):
        self.config = config
        self.path_cache = path_cache
        self.response = {}
        self.parse_response()
        self.limit = self.get_limit()

    @logging_dec
    def parse_response(self):
        """Define the structure of feeds

            Returns:

            """

        check_cache_file(self.path_cache)
        log.info('Cache checked: {}'.format(''))

        with open(self.path_cache, "r") as file:
            data = json.load(file)
            log.info('Cache read: {}'.format(data))

        got_data = {}

        if self.config['scenario'] == 'scenario 2: get news from cache with limit or without limit':
            for key, value in data.items():
                if str(self.config['date']) == value['publish_date']:
                    got_data[key] = value
        else:
            for key, value in data.items():
                if self.config['source'] == value['Source'] and str(self.config['date']) == value['publish_date']:
                    got_data[key] = value

        for key, value in got_data.items():
            feed = value['Feed']
            title = value['Title']
            date = value['Date']
            link = value['Link']
            links = value['Links']
            publish_date = value['publish_date']

            self.cash.append({publish_date: {'Feed': feed, 'Title': title, 'Date': date, 'Link': link, 'Links': links}})
            log.info('Got cash: {}'.format(self.cash))
            self.cash_json = json.dumps(self.cash)
            log.info('Got cash_json: {}'.format(self.cash_json))

    @logging_dec
    def get_limit(self):
        """Define the limit RSS

            Returns:
                limit
            """

        if self.config['limit']:
            if self.config['limit'] <= len(self.cash):
                log.info('Got limit: {}'.format(self.config['limit']))
                return self.config['limit']
            else:
                log.info('Got limit: {}'.format(len(self.cash)))
                return len(self.cash)
        else:
            limit = len(self.cash)
            log.info('Got limit: {}'.format(limit))
            return limit

    @logging_dec
    def print_rss(self):
        """Define the printing feeds

            Returns:

            """

        print('\n********** DATA FROM CACHE **********\n')

        if not self.cash:
            print("Not news for this date")
            return

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
