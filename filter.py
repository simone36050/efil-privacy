from json import load, dump

# settings

LIMIT_UNRECOGNIZED_PRINT = 60

# json

def load_subs() -> list:
    with open('subdomain1.json') as f:
        return load(f)

def dump_subs(subs: list):
    with open('subdomain2.json', 'w') as f:
        dump(subs, f)

# filter

def filter(rows: list):
    new = []
    for row in rows:
        if row['status'] == 'use_recaptcha':
            row['classification'] = None
            new.append(row)
    return new

def main():
    subs = load_subs()
    subs = filter(subs)
    dump_subs(subs)

if __name__ == '__main__':
    main()
