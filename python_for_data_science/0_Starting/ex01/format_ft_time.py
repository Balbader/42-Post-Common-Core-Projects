from time import time
from datetime import datetime

# Get current timestamp
seconds = time()

# Format the seconds with comma as thousand separator and 4 decimal places
formatted_seconds = "{:,.4f}".format(seconds)

# Format the seconds in scientific notation
scientific_notation = "{:.2e}".format(seconds)

# Get current date and format it
current_date = datetime.now().strftime("%b %d %Y")

# Print the formatted outputs
print(f"Seconds since January 1, 1970: {formatted_seconds} or\
      {scientific_notation} in scientific notation")
print(current_date)
