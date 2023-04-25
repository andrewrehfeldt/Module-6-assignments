import datetime


today = datetime.date.today()

with open("today.txt", "w") as f:
    f.write(str(today))


with open("today.txt", "r") as file:
    today_string = file.read()

parsed_date = datetime.datetime.strptime(today_string, "%Y-%m-%d").date()
print(parsed_date)