import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Get the content of this page with the "Requests" package.
result = requests.get('http://old-releases.ubuntu.com/releases/')

# Use the "BeautifulSoup" package to structure the retrieved content
# from an HTML page.
soup = BeautifulSoup(result.text, 'html.parser')

all_dates = []

# Get all "table" element in that page (there is only one in this case)
tables = soup.findAll("table")
for table in tables:
    rows = table.findAll('tr')

    for row in rows :
        tds = row.findAll('td')

        # We saw that on this page, the date are always on the 3rd rows.
        # We also make sure there is at least 3 elements so it won't crash
        # if the current row has less than 3.
        if len(tds) >= 3:

            # Convert the text into a DateTime object.
            # check documentation here:
            # https://www.tutorialspoint.com/python3/time_strptime.htm
            try:
                current_date = datetime.strptime(tds[2].text, '%Y-%m-%d %H:%M  ')
                all_dates.append(current_date)
            except Exception:
                # In case we are unable to parse the text into a date.
                # to prevent the app to crash.
                pass

# Get the biggest (latest) date from our list
latest_date = max(all_dates)

print('The latest date on this page is: {}'.format(latest_date))
