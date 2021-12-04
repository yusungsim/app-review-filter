from pprint import pprint

def int_dict_sum(d):
    sum = 0
    for _, i in d.items():
        sum += i
    return sum

def print_lex_db(lex, db):
    print(f'--- {lex} --- ')
    if lex not in db.keys():
        print('Not found')
        return
    sem_count = int_dict_sum(db[lex])
    print(f'Total: {sem_count}')
    sorted_pairs = sorted(db[lex].items(), key=lambda x: x[1], reverse=True)
    for desc, count in sorted_pairs[:10]:
        print(f'{desc} : {count}')
