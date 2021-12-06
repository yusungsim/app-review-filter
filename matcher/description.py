from tqdm import tqdm

# defines partial description semantic
def description(target, descriptor):
    return (target.strip().lower(), descriptor.strip().lower())

# parse each pattern to descriptor
def parse_aux(aux, attr, adj, nsubj):
    return description(attr, adj)

def parse_aux_line(line):
    toks = line.split(",")
    aux = toks[0]
    attr = toks[1]
    adj = toks[2]
    nsubj = toks[3]
    return parse_aux(aux, attr, adj, nsubj)

def parse_adj(noun, adj):
    return description(noun, adj)

def parse_adj_line(line):
    toks = line.split(",")
    noun = toks[0]
    adj = toks[1]
    return parse_adj(noun, adj)

# descriptor database
# desc_db: Map ( String -> Map (String -> Int))
def mk_desc_db():
    return dict()

def add_desc_db(db, desc):
    target, descriptor = desc
    if target not in db.keys():
        db[target] = dict()
    target_entry = db[target]
    if descriptor not in target_entry.keys():
        target_entry[descriptor] = 0
    target_entry[descriptor] += 1

# makes desc db for given appname
def make_desc_db(appname):
    pattern_names = ['AUX', 'ADJ']
    pattern_parsers = [parse_aux_line, parse_adj_line]

    db = mk_desc_db()

    for name, parser in tqdm(zip(pattern_names, pattern_parsers)):
        f = open("matches/" + appname + "_" + name + ".csv", 'r')
        for line in f:
            desc = parser(line)
            add_desc_db(db, desc)

    return db
