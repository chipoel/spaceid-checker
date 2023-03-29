import requests
import json
import threading

url = 'https://graphigo.prd.space.id/query'
headers = {
    'authority': 'graphigo.prd.space.id',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://space.id',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

max_threads = 1000
semaphore = threading.BoundedSemaphore(max_threads)

def get_domains(query):
    data = {
        'operationName': 'domains',
        'variables': {
            'input': {
                'query': query,
                'buyNow': 1,
                'domainStatuses': ['REGISTERED', 'UNREGISTERED'],
                'first': 30
            }
        },
        'query': 'query domains($input: ListDomainsInput!) { \
                    domains(input: $input) { \
                        exactMatch { \
                            name \
                            network \
                            owner \
                            listPrice \
                            expirationDate \
                            __typename \
                        } \
                    } \
                }'
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = json.loads(response.text)
    domains = response_json['data']['domains']['exactMatch']

    return domains

def process_query(query):
    try:
        domains = get_domains(query)

        for domain in domains:
            if not domain['owner'] and domain['expirationDate'] == 0 and domain['listPrice'] == 5:
                if domain['network'] == 0:
                    print(domain['name'] + '.eth', end='')
                elif domain['network'] == 1:
                    print(domain['name'] + '.bnb', end='')
                elif domain['network'] == 2:
                    print(domain['name'] + '.arb', end='')

                if 'listPrice' in domain:
                    print(' - List Price: ' + str(domain['listPrice']))
                else:
                    print(' - List Price: Not available')

                print()
    except Exception as e:
        pass
    finally:
        semaphore.release()


with open('combinations.txt', 'r') as f:
    queries = [line.strip() for line in f.readlines()]

threads = []
for query in queries:
    semaphore.acquire()
    t = threading.Thread(target=process_query, args=(query,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
