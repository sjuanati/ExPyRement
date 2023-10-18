import time

from libs.openexchange import OpenExchangeClient

import os
from dotenv import load_dotenv

load_dotenv()

client = OpenExchangeClient(os.getenv("APP_ID"))

eur_amount = 1

for _ in range(3):
    start = time.time()
    gbp_amount = client.convert(
        from_amount=eur_amount, from_currency="EUR", to_currency="USD"
    )
    end = time.time()
    print(end - start)

print(f"EUR{eur_amount} is USD{gbp_amount}")
