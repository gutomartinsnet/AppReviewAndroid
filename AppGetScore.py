from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument('--headless')
s = Service('C:\\webdrivers\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

url_score = 'https://play.google.com/store/apps/details?id=br.gov.sp.prodesp.pptdigital&hl=pt_BR&gl=US'

driver.get(url_score)
soup=BeautifulSoup(html_source, "html.parser")

review_score_src = soup.find('div', {'class','jILTFe'}).text
#print(review_score_src)

#review_score_list = []

#for val in review_score_src:
#    try:
#        review_score_list.append(val.get_text())
#    except:
#        pass
#review_score_list[:1]    

g_df = pd.DataFrame(np.array(review_author_list_src),columns=['review_score_src'])
g_df2 = g_df.join(pd.DataFrame(g_df.pop('review_score_src').tolist()))
g_df2.head()

g_df2.to_csv('pptdigital-appgoogle-reviews-score.csv',encoding='utf-8-sig')
#g_df.to_excel('pptdigital-appgoogle-reviews.xlsx', sheet_name='google play',encoding='utf-8-sig')
