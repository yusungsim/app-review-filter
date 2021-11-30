import spacy

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

