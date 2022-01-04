from json import dump, load

def main():
    # read
    with open('subdomain0.json') as f:
        subs = load(f)

    # clean
    subdomains = []
    for s in subs['subdomains']:
        subdomains.append({
            'domain': s['subdomain'],
            'status': 'not_tested'
        })

    # write
    with open('subdomain1.json', 'w') as f:
        dump(subdomains, f)

if __name__ == '__main__':
    main()
