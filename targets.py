def parse_apps(filename):
    with open(filename, 'r') as f:
        return [line.rstrip() for line in f]

if __name__ == "__main__":
    print(parse_apps())
