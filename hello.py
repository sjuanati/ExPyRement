import os
from dotenv import load_dotenv

load_dotenv()

msg = 'heyo wold'

print(f"I'd like to say {msg}")
print(os.getenv('ADMIN_EMAIL'))

