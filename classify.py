from json import load, dump

# settings

LIMIT_UNRECOGNIZED_PRINT = 800

# json

def load_subs() -> list:
    with open('subdomain2.json') as f:
        return load(f)

def dump_subs(subs: list):
    with open('subdomain2.json', 'w') as f:
        dump(subs, f)

# classify

def classify(domain: str) -> str:
    # comune
    if ('comune' in domain or 'unionedeicomuni' in domain or 'unione' in domain or 
            'comunita' in domain or 'citta' in domain):
        return 'comune'

    # orini
    if ('ordine' in domain or 'architetti' in domain or 'periti' in domain or
            'ingegneri' in domain or 'psicologi' in domain or 'geometri' in domain or
            'odcec' in domain or 'omceo' in domain or 'avvocati' in domain or
            'farmacisti' in domain or 'giornalisti' in domain or '.cdl.' in domain or
            '.opi.' in domain or 'ostetriche' in domain):
        return 'ordine'

    if ('srl' in domain or 'spa.' in domain or '.apm.' in domain or 'consorzio' in domain or
            'azienda' in domain or 'ospedale' in domain):
        return 'azienda'

    if 'provincia' in domain or 'bnl' in domain:
        return 'altro'

    # other
    return None

def classify_all(rows: list):
    unrec = 0
    for row in rows:
        if row['classification'] == None:
            classification = classify(row['domain'])

            if classification != None:
                row['classification'] = classification
            else:
                if unrec < LIMIT_UNRECOGNIZED_PRINT:
                    print(row['domain'])
                    unrec += 1
        
def main():
    subs = load_subs()
    classify_all(subs)
    dump_subs(subs)

if __name__ == '__main__':
    main()
