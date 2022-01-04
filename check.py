from requests import get
from json import load, dump
from time import sleep

# settings

SLEEP_BETWEEN_CHECKS = 0.8 # seconds
REQUEST_TIMEOUT = 15
LOG_CHECKS = True
CHECK_AMOUNT = 60

# json

def load_subs() -> list:
    with open('subdomain1.json') as f:
        return load(f)

def dump_subs(subs: list):
    with open('subdomain1.json', 'w') as f:
        dump(subs, f)

# check

def check(domain: str) -> str:
    try:
        res = get('https://{}/'.format(domain), timeout=REQUEST_TIMEOUT)
    except Exception as e:
        if 'Name or service not known' in str(e):
            return 'no_dns'
        return 'error|' + str(e)
    
    if res.status_code != 200:
        return 'non_200|{}'.format(res.status_code)

    if 'Benvenuto nel portale dei pagamenti'.lower() not in res.text.lower():
        return 'non_payment_website'

    if "<script src='https://www.google.com/recaptcha/api.js'></script>" in res.text:
        return 'use_recaptcha'

    return 'good'

def check_multiple(rows: list):
    for row in rows:
        domain = row['domain']

        if LOG_CHECKS:
            print('Check {}: '.format(domain), end='', flush=True)

        status = check(domain)
        row['status'] = status

        if LOG_CHECKS:
            print(status)

        sleep(SLEEP_BETWEEN_CHECKS)

# main

def get_non_tested(subs: list, amount: int = CHECK_AMOUNT):
    result = []
    for s in subs:
        if s['status'] == 'not_tested' and len(result) < amount:
            result.append(s)
    return result


def main():
    subs = load_subs()
    to_check = get_non_tested(subs)
    check_multiple(to_check)
    dump_subs(subs)

if __name__ == '__main__':
    main()
