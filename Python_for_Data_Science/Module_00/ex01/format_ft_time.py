from time import time
from datetime import datetime

print(f"Seconds since January 1, 1970: {time():,.4f} or",
      f"{time():.2e} in scientific notation")
print(datetime.now().strftime("%b %d %Y"))
