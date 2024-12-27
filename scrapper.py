from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from pymongo import MongoClient
from datetime import datetime



# options = Options()
# options.add_argument("--proxy-server=http://Chetan77:Tiet@2025@de.proxymesh.com:31280")


client = MongoClient('mongodb://localhost:27017/')  
db = client['twitter_trends']
collection = db['trends']


driver = webdriver.Chrome()

try:
   
    driver.get("https://x.com/login")
    time.sleep(3)

    username = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
    username.send_keys("DongareChetan77")
    username.send_keys(Keys.RETURN)
    time.sleep(2)

    password = driver.find_element(By.NAME, "password")
    password.send_keys("Tiet@2025")
    password.send_keys(Keys.RETURN)
    time.sleep(5)

    
    driver.get("https://twitter.com/explore/tabs/trending")
    time.sleep(5)

    
    print("Top 5 Trending Topics on Twitter:")
    trends = []
    for i in range(1, 6):
        selector = f"#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div > section > div > div > div:nth-child({i})"
        try:
            element = driver.find_element(By.CSS_SELECTOR, selector)
            trend = element.text.strip()
            print(f"{i}. {trend}")
            trends.append({"rank": i, "trend": trend, "timestamp": datetime.now()})
        except Exception as e:
            print(f"{i}. [Trend not found]")

    
    if trends:
        unique_id = str(time.time())
        trends_doc = { "_id": unique_id, "trend1": trends[0]['trend'], "trend2": trends[1]['trend'], "trend3": trends[2]['trend'], "trend4": trends[3]['trend'], "trend5": trends[4]['trend'], "timestamp": datetime.now(), "ip_address": "XXX.XXX.XXX.XXX" }
        collection.insert_one(trends_doc)
        print("Trends saved to MongoDB.")

finally:
    driver.quit()
