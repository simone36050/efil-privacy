from json import load
from pprint import pprint

# json

def load_subs(n: int) -> list:
    with open('subdomain{}.json'.format(n)) as f:
        return load(f)

# domains

def domains():
    doms = load_subs(1)
    data = {
        'no_dns': 0,
        'non_200': 0,
        'non_payment_website': 0,
        'use_recaptcha': 0,
        'error': 0
    }

    for dom in doms:
        status = dom['status']

        if 'use_recaptcha' == status:
            data['use_recaptcha'] += 1

        elif 'non_payment_website' == status:
            data['non_payment_website'] += 1

        elif 'no_dns' == status:
            data['no_dns'] += 1

        elif 'non_200|' in status:
            data['non_200'] += 1

        elif 'error|' in status:
            data['error'] += 1

        else:
            print('Error {}'.format(status))

    return data

# classifications

def classifications():
    doms = load_subs(2)
    data = {}

    for dom in doms:
        if dom['classification'] in data:
            data[dom['classification']] += 1
        else:
            data[dom['classification']] = 1

    return data

# main

def main():
    print('Domains:')
    pprint(domains())

    print('Classifications:')
    pprint(classifications())

if __name__ == '__main__':
    main()
