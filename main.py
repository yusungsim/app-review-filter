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

nouns = ['NOUN', 'PROPN']
verbs = ['VERB', 'AUX']
adjectives = ['ADJ']
adverbs = ['ADV']

lex_dict_kinds = [dict(), dict(), dict(), dict()]
for app in appnames:
    reviews = get_reviews(app)
    gather_lexicon(lex_dict_kinds[0], reviews, nouns)
    gather_lexicon(lex_dict_kinds[1], reviews, verbs)
    gather_lexicon(lex_dict_kinds[2], reviews, adjectives)
    gather_lexicon(lex_dict_kinds[3], reviews, adverbs)

dump_lexicon(lex_dict_kinds[0], 'lexicon_noun.csv')
dump_lexicon(lex_dict_kinds[1], 'lexicon_verb.csv')
dump_lexicon(lex_dict_kinds[2], 'lexicon_adjective.csv')
dump_lexicon(lex_dict_kinds[3], 'lexicon_adverbs.csv')

"""
for review in reviews:
    print(f'Review: "{review}"')
    doc = nlp(review)
    for tok in doc:
        print(tok.lemma_, tok.pos_, end=" | ")
    print()
    input()
"""
