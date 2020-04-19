import requests
import argparse
import os
import json
import datetime
from _validations import is_date_valid, code_error


class Client(object):
    def __init__(self):
        self.base_url = "https://api.coinpaprika.com/v1/"
        self.parser = argparse.ArgumentParser(description="Process requests for paprikacoin API data")
        self.parser.add_argument('--today', action='store', dest='coin',
                           help="Get today data of specific coin - pass coin_id")
        self.parser.add_argument('--history', action='store', nargs='+', dest='coin_history',
                           help="Get historical data of specific coin - pass [coin-id] [history start date] YYYY-MM-DD")

    def process(self):
        args = self.parser.parse_args()
        if args.coin:
            self.today_coin(args.coin)

        elif args.coin_history:
            coin_id, start_date = args.coin_history
            print(coin_id, start_date)
            self.coin_history(coin_id, start_date)

    def today_coin(self, coin_id: str) -> None:
        get_coin_url = os.path.join(self.base_url, "coins")
        daily_coin = requests.get(url=get_coin_url, params={"coin-id": coin_id})

    def coin_history(self, coin_id: str, start_date: str):
        if is_date_valid(start_date):
            get_coin_history_url = os.path.join(self.base_url, 'tickers', coin_id, 'historical')
            coin_history = requests.get(url=get_coin_history_url, params={"start": start_date})
            code_error(coin_history.status_code)
            cur_datetime = datetime.datetime.now()
            filename = "{}_from_{}_to_{}.json".format(coin_id, start_date, cur_datetime.strftime("%Y-%m-%d"))
            with open(f"data/{filename}", 'w') as fp:
                json.dump(coin_history.json(), fp)


if __name__ == '__main__':
    client = Client()
    client.process()



