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

def get_total_count(db):
    sum = 0
    for nouns in db.keys():
        for desc, count in db[nouns].items():
            sum += count
    return sum

def get_total_cluster_count(cluster_dict):
    sum = 0
    for desc, count in cluster_dict.items():
        sum += count
    return sum

def print_cluster_db(cluster_name, cluster_dict, demo=False):
    if len(cluster_dict) == 0:
        print(f'Description on {cluster_name} Not Found')
        print('---------------------------------------')
        return

    cluster_count = get_total_cluster_count(cluster_dict)
    print(f'Total {cluster_count} Descriptions for {cluster_name}')
    print(f'[Description Summary]')

    sorted_pairs = sorted(cluster_dict.items(), key=lambda x: x[1], reverse=True)
    for desc, count in sorted_pairs[:5]:
        percentage = "{:.2f}".format(count/cluster_count * 100.0)
        print(f'  {desc}: {count} ({percentage}%)')

    print('---------------------------------------')
    if demo:
        input('Press any key for next cluster summary...')
        print("\033[A                                          \033[A")
    return
