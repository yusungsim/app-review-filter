# libraries
import spacy
from tqdm import tqdm
from pprint import pprint

# custom imports
from scraper.scraper import store_reviews
from targets import parse_apps
from lexicon import gen_lexicons
from data_loader import get_reviews
from matcher.matcher import * 

# generate list of target app names
targetfile = 'paid-top-45-Nov-30'
appnames = parse_apps(targetfile)

# generate review data for each app  
print("Generating Review data...")
for appname in tqdm(appnames):
    store_reviews(appname)

# generate lexicon csv files on `lex` directory
print("Generating lexicons...")
gen_lexicons(appnames)

# generate matched patterns on `matches` directory
print("Generating matches...")
for appname in tqdm(appnames):
    reviews = get_reviews(appname)
    aux_match_list(appname, reviews)
    verb_match_list(appname, reviews)
    adj_match_list(appname, reviews)

# parse the patterns into semantic description, and 
