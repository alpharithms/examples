
"""
Initial examples of datetime usage
"""
from datetime import datetime
# Create a datetime object
dto = datetime.now()

# Convert to string
dto_string = dto.strftime("%Y-%m-%d")
print(dto, type(dto))
print(dto_string, type(dto_string))

"""
Convert a string to a datetime object, 
"""
from datetime import datetime

# Create a string datetime
date = "2022-06-17T18:23:59"

# Convert to naive datetime object
date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
print(date, type(date))

"""
Convert a string to a datetime object
"""
from datetime import datetime, timezone

# Create a datetime object using explicit arguments
date = datetime(
    year=2022,
    month=6,
    day=17,
    hour=18,
    minute=23,
    second=59,
    tzinfo=timezone.utc
)
print(date, type(date))

# Convert to string using formatting syntax
date = date.strftime("%Y-%m-%dT%H:%M:%S %Z%z")
print(date, type(date))

"""
Convert a string to a datetime object, adding timezone information
"""
from datetime import datetime, timezone

# Create a string datetime
date = "2022-06-17T18:23:59"

# Convert to naive datetime object
date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")

# Add UTC Timezone Info
date.replace(tzinfo=timezone.utc)
print("Initial Timezone:", date.tzinfo)

# Add UTC Timezone w/ Assignment
date = date.replace(tzinfo=timezone.utc)
print("Updated Timezone:", date.tzinfo)

# Convert to Timezone Format
tz_date = date.strftime("%Y-%m-%dT%H:%M:%S %Z%z")
print("Converted Timezone:", tz_date)