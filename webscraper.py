import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Edge(executable_path="C:/Users/bdhai/OneDrive/Desktop/msedgedriver.exe")

driver.get("https://oxylabs.io/blog")
results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for element in soup.findAll(attrs="css-1l2kada e16chy464"):
    name = element.find("a href")
    if name not in results:
        results.apend(name.text)

df = pd.DataFrame({"Names": results})
df.to_csv("names.csv", index=False, encoding="utf-8")
