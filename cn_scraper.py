from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get("https://wearecodenation.com/2024/01/23/data-course-playground/").text
soup = BeautifulSoup(html_text, "lxml")

h5s = soup.find_all("h5", class_="elementor-heading-title elementor-size-default")

course_dates = {}

for h5Tag in h5s:
    if ":" in h5Tag.text:
        #print(h5Tag.text)
        course_dates[h5Tag.text] = []
        dates = h5Tag.find_next("h6")
        #print(dates.text)
        for single_date in dates.strings:
            #print(single_date)
            course_dates[h5Tag.text].append(single_date)

print(course_dates)

# h6s = soup.find_all("h6")

# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# course_dates = []

# for h6Tags in h6s:
    # if any(month in h6Tags.text for month in months):
        # print(h6Tags.text)
        # course_dates.append(h6Tags.text)
    
# print(course_dates)

#ACTIVITY 2

# mySeries = pd.Series([""])

updated_dates = {key: pd.Series(value) for key, value in course_dates.items()}

df = pd.DataFrame(updated_dates)

print(df)