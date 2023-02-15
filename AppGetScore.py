#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.service import Service
import requests
import pandas as pd
import numpy as np

#options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#s = Service('C:\\webdrivers\\chromedriver.exe')
#driver = webdriver.Chrome(service=s, options=options)

url_score = 'https://play.google.com/store/apps/details?id=br.gov.sp.prodesp.pptdigital&hl=pt_BR&gl=US'

res =  requests.get(url_score)
#res = requests.get(url)
html_source = res.text
soup=BeautifulSoup(html_source, "html.parser")

review_score_src = soup.find_all('div', {'class','jILTFe'})
#print(review_score_src)

review_score_list = []
for val in review_score_src:
    try:
        review_score_list.append(val.get_text())
    except:
        pass
review_score_list[:0]    

g_df = pd.DataFrame(np.array(review_score_list),columns=['review_score_src'])
print(g_df)
g_df.to_csv('pptdigital-appgoogle-reviews-score.csv')
#g_df.to_excel('pptdigital-appgoogle-reviews.xlsx', sheet_name='google play',encoding='utf-8-sig')
