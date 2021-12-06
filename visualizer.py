import spacy
from spacy import displacy
from data_loader import get_reviews

nlp = spacy.load("en_core_web_sm")

def visualize_text(text):
   doc = nlp(text)
   displacy.serve(doc)

def has_words(words, text):
    for word in words:
        if word in text:
            return True
    return False

if __name__ == "__main__":
    review = input() 
    reviews = [review]
    target_words = [
        'game',
        'app',
        'gameplay',
        'money',
        'price',
        'bug',
        'story',
        'character',
        'graphics',
        'update',
    ]

    for review in reviews:
        #if not has_words(target_words, review):
        #    continue
        print(review)
        visualize_text(review)
        input()
