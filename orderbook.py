import requests
import csv
import time
from datetime import datetime

class UpbitOrderBookCollector:
    def __init__(self, market_name, interval=5):
        self.market_name = market_name
        self.interval = interval

    def fetch_order_book(self):
        url = f"https://api.upbit.com/v1/orderbook?markets={self.market_name}"
        response = requests.get(url)
        order_book_data = response.json()[0]
        return order_book_data

    def save_order_book(self, order_book_data, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['price', 'quantity', 'type', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for bid in order_book_data['orderbook_units']:
                writer.writerow({'price': bid['ask_price'], 'quantity': bid['ask_size'], 'type': 'bid', 'timestamp': time.time()})
            for ask in order_book_data['orderbook_units']:
                writer.writerow({'price': ask['bid_price'], 'quantity': ask['bid_size'], 'type': 'ask', 'timestamp': time.time()})

    def run(self):
        while True:
            order_book_data = self.fetch_order_book()
            filename = f"book-{datetime.now().strftime('%Y-%m-%d')}-upbit-{self.market_name}.csv"
            self.save_order_book(order_book_data, filename)
            print(f"Order book data saved to {filename}")
            time.sleep(self.interval)

# Usage example:
if __name__ == "__main__":
    collector = UpbitOrderBookCollector(market_name='KRW-BTC', interval=5)
    collector.run()

