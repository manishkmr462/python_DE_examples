# necessary imports
from datetime import datetime
from datetime import timedelta
from datetime import timezone
# take input from the user

print("Welcome to time application")
option = input("""Enter an option:
(1. Current time)
(2. Current UTC time)
(3. Current EST time)""")

option = int(option)

print(f"The option entered is: {option}")

if option == 1:
    print(f"Currrent time is: {datetime.now()}")
elif option == 2:
    utc_time_zone = timezone(offset=timedelta(),name="UTC")
    print(f"Currrent time is: {datetime.now(tz=utc_time_zone)}, time_zone is: {utc_time_zone}")
elif option == 3:
    est_time_zone = timezone(offset=timedelta(hours=-5),name="EST")
    print(f"Currrent time is: {datetime.now(tz=est_time_zone)}, time_zone is: {est_time_zone}")


