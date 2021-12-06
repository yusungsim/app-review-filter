from tqdm import tqdm

def parse_apps(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(line.rstrip())        
    return result

if __name__ == "__main__":
    print(parse_apps())
