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
from matcher.description import *
from summarize import *

def cache_call():
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

def merge_cluster_db(cluster, db):
    result = dict()
    for noun in cluster:
        if noun not in db.keys():
            continue

        noun_desc_dict = db[noun]
        for desc in noun_desc_dict.keys():
            cur_count = noun_desc_dict[desc]
            if desc in result.keys():
                result[desc] += cur_count
            else:
                result[desc] = cur_count 
    return result

# parse the patterns into semantic description, and 
def main():
    print('Parsing Cached App names...')
    targetfile = 'paid-top-45-Nov-30'
    appnames = parse_apps(targetfile)

    appname = input('Input app name(ex: `com.mojang.minecraftpe`):')

    if appname not in appnames:
       print("Not valid appname; review data must be cached")
       return
   
    print("Fetching Review data...")
    store_reviews(appname)

    print("Generating matches..")
    reviews = get_reviews(appname)
    all_match_list(appname, reviews)

    print(f"Generating semantic db for {appname}...")
    db = make_desc_db(appname)
    
    print('Summary of Description Semantics for each cluster') 
    cluster_names = ['Overall', 'Content', 'Graphics',
                     'Pricing', 'Functionality', 'Update']
    cluster_app = ['game', 'app']
    cluster_content = ['story', 'character', 'gameplay']
    cluster_graphics = ['graphics', 'screen']
    cluster_pricing = ['money', 'price']
    cluster_funct = ['bug', 'issue']
    cluster_update = ['update', 'version']
    clusters = [cluster_app, cluster_content, 
                cluster_graphics, cluster_pricing, 
                cluster_funct, cluster_update]

    result_dbs = []
    for cluster in clusters:      
        result_dbs.append(merge_cluster_db(cluster, db)) 

    total_count = get_total_count(db)
    print(f'Total {total_count} Descriptions Extracted')
    print('===========================================')
    for cluster_name, cluster_db in zip(cluster_names, result_dbs):
        print_cluster_db(cluster_name, cluster_db, demo=True)

if __name__ == '__main__':
    main()
