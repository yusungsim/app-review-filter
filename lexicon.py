import spacy
from data_loader import get_reviews

def gather_lexicon(lex_dict, sent_list, target_pos):
    nlp = spacy.load("en_core_web_sm")

    def add_lexicon(word):
        if word in lex_dict.keys():
            lex_dict[word] = lex_dict[word] + 1
        else:
            lex_dict[word] = 1

    for sent in sent_list:
        doc = nlp(sent)
        for tok in doc:
            if tok.pos_ in target_pos:
                add_lexicon(tok.lemma_)

def dump_lexicon(lex_dict, filename):
    lex_sorted = sorted(lex_dict.items(), key= lambda x: x[1], reverse=True)
    with open(filename, 'w') as f:
        for (word, count) in lex_sorted:
            f.write(f'{word}, {count}\n') # csv format     

def gen_lexicons(appnames):
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

    dump_lexicon(lex_dict_kinds[0], 'lex/lexicon_noun.csv')
    dump_lexicon(lex_dict_kinds[1], 'lex/lexicon_verb.csv')
    dump_lexicon(lex_dict_kinds[2], 'lex/lexicon_adjective.csv')
    dump_lexicon(lex_dict_kinds[3], 'lex/lexicon_adverbs.csv')
