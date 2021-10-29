from pprint import pprint
from scraper.scraper import store_reviews

ex_apps = ['com.fantome.penguinisle', 'com.spotify.music', 'com.nianticlabs.pokemongo']

for appname in ex_apps:
    store_reviews(appname)

