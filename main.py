# libraries
import spacy
from pprint import pprint

# custom imports
from scraper.scraper import store_reviews
from targets import parse_apps
from lexicon import gen_lexicons


# generate list of target app names
targetfile = 'paid-top-45-Nov-30'
appnames = parse_apps(targetfile)

# generate review data for each app  
for appname in appnames:
    store_reviews(appname)

# generate lexicon csv files on `lex` directory
gen_lexicons(appnames)
