from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%y")
print("year:", year)