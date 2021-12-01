import spacy
from spacy import displacy
from spacy.matcher import DependencyMatcher
from data_loader import get_reviews

nlp = spacy.load("en_core_web_sm")
matcher = DependencyMatcher(nlp.vocab)

def aux_adj_pattern(target_noun_list):
    pattern = [
        # anchor: aux verb
        {
            "RIGHT_ID": "aux",
            "RIGHT_ATTRS": {"ORTH": "is"}
        },
        # matching the subject noun
        {
            "LEFT_ID": "aux",
            "REL_OP": ">",
            "RIGHT_ID": "subj",
            "RIGHT_ATTRS": {
                "POS": "NOUN",
                "LEMMA": {"IN": target_noun_list},
            },
        },
        # matching the adjective
        {
            "LEFT_ID": "aux",
            "REL_OP": ">",
            "RIGHT_ID": "adjective",
            "RIGHT_ATTRS": {"DEP": "acomp"},
        },
    ]
    return pattern

def nvn_pattern(target_noun_list):
    pattern = [
        {
            "RIGHT_ID": "verb",
            "RIGHT_ATTRS": {"POS": "VERB"},
        },
        {
            "LEFT_ID": "verb",
            "REL_OP": ">",
            "RIGHT_ID": "obj",
            "RIGHT_ATTRS": {
                "POS": "NOUN",
                "LEMMA": {"IN": target_noun_list},
            },
        }
    ]
    return pattern

# general matcher for pattern
# first-class 'pattern'
def try_match(pattern, doc):
    matcher.add("pattern", [pattern])
    matches = matcher(doc)

    for match_id, token_ids in matches:
        print(f'---- match_id:{match_id} ----')
        for i in range(len(token_ids)):
            print(pattern[i]["RIGHT_ID"] + ":", doc[token_ids[i]].text)

    matcher.remove("pattern")
    return matches

# test code
if __name__ == '__main__':
    appname = 'com.mojang.minecraftpe' 
    reviews = get_reviews(appname) 
    
    # make pattern
    target_nouns = ['game', 'app', 'story', 'control', 'character', 'graphic', 'music']

    aux_pattern = aux_adj_pattern(target_nouns)
    verb_pattern = nvn_pattern(target_nouns)

    for review in reviews:
        review_doc = nlp(review)
        try_match(aux_pattern, review_doc)
        try_match(verb_pattern, review_doc)

# displacy.serve(doc, style="dep")
