
import time  # use time.sleep(number of seconds) to wait between requests
import requests
import json
from os import path, makedirs


''' Global Settings '''
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
sleep_time=11
debug = True
cached_results = True


def get_raw_address(address, cached=cached_results):
    ''' Return JSON response of raw address. Optionally uses cache.'''

    local_filename = "test_data/" + address + ".json"
    # Does not query website if cached in local filesystem
    if cached:
        if path.exists(local_filename):
            with open(local_filename) as file:
                json_response = json.load(file)
            return json_response

    baseurl = 'https://blockchain.info/rawaddr/'

    time.sleep(sleep_time)
    if debug:
        print("Querying for: " + address)
    r = requests.get(baseurl+address, headers=headers)
    json_response = json.loads(r.text)

    # print(json.dumps(json_response, indent = 4, sort_keys=True))

    # Cache response to local filesystem
    with open(local_filename, 'w') as json_file:
        json.dump(json_response, json_file)

    return json_response


def find_shared_spending(address):
    ''' Identifies and returns set of addresses which share this address as a transaction input '''
    linked_addresses = set()

    json_response = get_raw_address(address)

    base_address = json_response['address']
    transactions = json_response['txs'][:50] # Limited to first 50 transactions

    for transaction in transactions:
        # Get set of all input addresses for this transaction
        try:
            input_addresses = [input_item['prev_out']['addr'] for input_item in transaction['inputs']]
            input_addresses = set(input_addresses)

            if base_address in input_addresses: # and len(input_addresses) > 1:
                linked_addresses.update(input_addresses)
        except:
            if debug:
                print(transaction['inputs'])
            print("Program exited due to error: -1")
            exit(-1)
    
    return linked_addresses


def get_final_balances(address_set):
    ''' Returns JSON of final balance queries '''
    baseurl = 'https://blockchain.info/balance?active='

    query = "|".join(address_set)

    if debug:
        print("Querying balances..")
    time.sleep(sleep_time)
    r = requests.get(baseurl+query, headers=headers)
    json_response = json.loads(r.text)

    return json_response


def print_balances(balance_json, print_all=debug):
    total = []
    for key, value in balance_json.items():
        if print_all:
            print(str(key) + "\t " + str(value['final_balance']))
        total.append(int(value['final_balance']))
    print("Balance for all linked address:\t\t", sum(total) / 100000000, " BTC (", sum(total), "Satoshis)")


def ensure_dir(file_path):
    directory = path.dirname(file_path)
    if not path.exists(directory):
        makedirs(directory)


def main(address, recursive=True):
    checked_addresses = set()
    to_check = set()

    ensure_dir('./test_data')

    # First pass for linked addresses
    linked_addresses = find_shared_spending(address)

    if recursive:
        checked_addresses.add(address)
        to_check = linked_addresses - checked_addresses

        # Loop will only break when all linked addresses have been checked
        while len(to_check) > 0:
            for linked_address in to_check:
                new_linked_addresses = find_shared_spending(linked_address)

                # Add newly discovered linked addresses to set
                linked_addresses.update(new_linked_addresses)
                # Do not check address again
                checked_addresses.add(linked_address)

            to_check = linked_addresses - checked_addresses
            # to_check.pop()

    print("Results for address:\t\t\t", address)
    print("Total linked addresses:\t\t\t", len(linked_addresses))

    balances_json = get_final_balances(linked_addresses)

    print_balances(balances_json)


if __name__=="__main__":

    address_list=[
        # '15hzoz4YzGnj9Pqu8eNmhw4tBpDGjNgwj9',
        '36bt43aDDvsMJRd48YiRh6LLrNm3qnGZW5',
        '19ere2oJzJh81A5Q64SExDZYz54RvWHqZz',
        '19QDGMRKdZ9BpDZP2Re6yaDqNQ7zN4wo1D'
        ]

    for address in address_list:
        main(address)
        print()
