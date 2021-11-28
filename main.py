from pprint import pprint
from scraper.scraper import store_reviews
from targets import parse_apps
from data_loader import get_reviews 
import spacy

targetfile = 'target-apps'
appnames = parse_apps(targetfile)

for appname in appnames:
    store_reviews(appname)

app0 = appnames[0]
reviews = get_reviews(app0)

# print(app0, reviews0)

review0 = reviews[3]
print(review0)

nlp = spacy.load("en_core_web_sm")
doc = nlp(review0)

for token in doc:
    print(token, token.lemma_, token.pos_)
