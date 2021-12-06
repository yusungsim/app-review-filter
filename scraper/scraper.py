from google_play_scraper import Sort, reviews_all, reviews
import os
from tqdm import tqdm

# number of reviews fetched per app
REVIEW_COUNT = 1000

# get_reviews: str -> list[str]
def get_reviews(appname):
    #print(f'get_reviews: called with appname={appname}')
    #print('get_reviews: start fetching..')
    fetched, _ = reviews(appname, count=REVIEW_COUNT)
    #print('get_reviews: data fetched')
    
    res = []
    for rev in fetched:
        res.append(rev['content'])

    #print('get_reviews: returning')
    return res

def store_reviews(appname):
    ##print(f'store_reviews: called with appname={appname}')
    ##print('store_reviews: calling get_reviews')
    ##print(f'store_reviews: got {l} reviews')
    ##print('store_reviews: writing reviews into file')
    datapath = 'data/' + appname 
    if (os.path.isfile(datapath)):
        print('>>> cached review data found; skipping fetching process...')
        pass
    else: 
        revs = get_reviews(appname)
        with open(datapath, 'w') as f:
            for rev in tqdm(revs):
                f.write(rev)
                f.write('\n')
    #print('store_review: returning')
    return
