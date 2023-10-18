import requests
import functools

from cachetools import cached, TTLCache

FIFTEEN_MINUTES = 15 * 60

"""
@functools.lru_cache(maxsize=2)
    maxsize=2 means that the cache will only ever store the results of the two most recent
    unique calls to the function. If a third unique call is made, the result of the least
    recently used of the previous two calls will be discarded from the cache.

cache=TTLCache(maxsize=2, ttl=900)
    `maxsize`=2: This specifies that the cache will store results for at most 2 unique function calls.
    `ttl`=900: This means each cached result will expire 900 seconds (or 15 minutes) after it was first created.
                Once a cache entry is older than this time-to-live, it's considered expired and will be discarded
                if accessed (and the function will be called again to produce a fresh result).
"""


class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api"

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    # @functools.lru_cache(maxsize=2) # option 1
    @cached(
        cache=TTLCache(maxsize=2, ttl=FIFTEEN_MINUTES)
    )  # every 15 minutes will update the value,
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()

    def convert(self, from_amount, from_currency, to_currency):
        rates = self.latest["rates"]
        to_rate = rates[to_currency]

        if from_currency == "USD":
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / rates[from_currency]
            return from_in_usd * to_rate
