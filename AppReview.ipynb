import pandas as pd #install pandas
import numpy as np #isntall numpy
from google_play_scraper import Sort, reviews_all #install google_play_scraper

result = reviews_all(
    'ID_app', #your ID url play.google after ?id=
    sleep_milliseconds=0, # defaults to 0
    lang='pt_BR', # defaults to 'en'
    country='br', # defaults to 'us'
    #sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    #filter_score_with=5 # defaults to None(means all score)
)

g_df = pd.DataFrame(np.array(result),columns=['review'])
g_df2 = g_df.join(pd.DataFrame(g_df.pop('review').tolist()))
g_df2.head()

g_df2.to_csv('appandroid-reviews.csv',encoding='utf-8-sig')
