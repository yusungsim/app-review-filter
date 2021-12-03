import spacy
from .aux_pattern import aux_pattern
from .verb_pattern import verb_pattern
from .adj_pattern import adj_pattern
from spacy.matcher import DependencyMatcher

nlp = spacy.load("en_core_web_sm")
matcher = DependencyMatcher(nlp.vocab)

# general matcher for pattern and text list
def store_match_list(pattern_name, pattern, text_list, column=None):
    matcher.add("pattern", [pattern])
    store_filename = "matches/" + pattern_name + ".csv"
    
    if column != None:
        with open(store_filename, 'w') as f:
            for t in column:
                f.write(t + ', ')
            f.write('\n')

    for text in text_list:
        doc = nlp(text)
        matches = matcher(doc)
        store_matches(pattern, doc, matches, store_filename)

    matcher.remove("pattern")

def print_matches(pattern, doc, matches):
    for match_id, token_ids in matches:
        print(f'-----------------------------')
        for i in range(len(token_ids)):
            print(pattern[i]["RIGHT_ID"] + ":", doc[token_ids[i]].text)

def store_matches(pattern, doc, matches, filename):
    with open(filename, 'a') as f:
        for match_id, token_ids in matches:
            for i in range(len(token_ids)):
                f.write(doc[token_ids[i]].text + ", ")
            f.write("\n")

# matchers for each pattern
def aux_match_list(appname, reviews):
    store_match_list(appname+"_AUX", aux_pattern, reviews,
            column=['AUX', 'ATTR', 'ADJ', 'NSUBJ'])

def verb_match_list(appname, reviews):
    store_match_list(appname+"_VERB", verb_pattern, reviews,
            column=['VERB', 'PREP', 'POBJ'])

def adj_match_list(appname, reviews):
    store_match_list(appname+"_ADJ", adj_pattern, reviews,
            column=['NOUN', 'ADJ'])
