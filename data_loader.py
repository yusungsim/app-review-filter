def get_reviews(appname):
    datapath = 'data/' + appname
    with open(datapath, 'r') as f:
        return [line.rstrip() for line in f]
