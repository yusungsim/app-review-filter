from pprint import pprint
from scraper.scraper import store_reviews
from targets import parse_apps
from data_loader import get_reviews 
from lexicon import gather_lexicon, dump_lexicon
import spacy

targetfile = 'paid-top-45-Nov-30'
appnames = parse_apps(targetfile)

for appname in appnames:
    store_reviews(appname)

app0 = appnames[0]
reviews = get_reviews(app0)

# print(app0, reviews0)

lex_dict = dict()
for app in appnames:
    reviews = get_reviews(app)
    gather_lexicon(lex_dict, reviews)

dump_lexicon(lex_dict, 'lexicon.csv')

"""
for review in reviews:
    print(f'Review: "{review}"')
    doc = nlp(review)
    for tok in doc:
        print(tok.lemma_, tok.pos_, end=" | ")
    print()
    input()
"""
