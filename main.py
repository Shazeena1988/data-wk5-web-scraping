from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get("https://www.scrapethissite.com/pages/simple/")

souped_html = BeautifulSoup(html_text.text, "lxml")

countries = souped_html.find_all("h3")

country_capitals = souped_html.find_all(class_="country-capital") 

country_population = souped_html.find_all("span" , class_="country-population")

df = pd.DataFrame({
    "Country": [country.text.strip() for country in countries],
    "Capital": [capital.text for capital in country_capitals],
    "Population": [population.text for population in country_population]
})

df = df.set_index("Country")

df.to_excel("country_output.xlsx")

print(df)