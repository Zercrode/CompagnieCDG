from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")
option.add_argument("disable-gpu")
data=[]
df = pd.DataFrame(data)
browser = webdriver.Chrome(executable_path='chromedriver', options=option)
browser.get("https://cdgfacile.com/quel-terminal-roissy-cdg/")
for i in range(0,21):
    s = pd.read_html(browser.page_source,index_col=False)[i]
    df=pd.concat([df,s])
browser.close()
df=df.dropna()
df=df.rename(columns={0: "Compagnie",1: "Code Compagnie", 2: "Terminal"})
df=df.set_index('Compagnie')
df
