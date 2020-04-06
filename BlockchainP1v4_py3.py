'''
Finds BTC addresses with shared spending and outputs balances of all shared addresses

Uses API from Blockchain.info

Set global settings near the top of the file
Set address list to check at the bottom of the file

Arghya Mukherjee
Codi West
'''

import time  # use time.sleep(number of seconds) to wait between requests
import requests
import json
from os import path, makedirs


''' Global Settings '''
# For use with requests package
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
# Time between queries
sleep_time=11
# Prints extra information
debug = True
# Will use local JSON if already queried and downloaded
cached_results = True
# Continues past single depth of linked addresses
recursive = True
# Stop recursive searching at given depth (only if recursive is enabled)
depth_limit = None


def get_raw_address(address, cached=cached_results):
    '''
    Return JSON response of raw address

    Saves JSON response to disk 
    Optionally uses cached saved response if possible
    '''

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
    '''
    Identifies and returns set of addresses which share this address as a transaction input

    Input addresses differing from the input['prev_out']['addr'] format are ignored
    '''
    linked_addresses = set()

    json_response = get_raw_address(address)

    base_address = json_response['address']
    transactions = json_response['txs'][:50] # Limited to first 50 transactions

    for transaction in transactions:
        # Get set of all input addresses for this transaction
        try:
            # input_addresses = [input_item['prev_out']['addr'] for input_item in transaction['inputs']]
            input_addresses = []
            for input_item in transaction['inputs']:
                if 'prev_out' in input_item.keys():
                    if 'addr' in input_item['prev_out'].keys():
                        input_addresses.append(input_item['prev_out']['addr'])

            input_addresses = set(input_addresses)

            if base_address in input_addresses: # and len(input_addresses) > 1:
                linked_addresses.update(input_addresses)
        except:
            if debug:
                print(transaction['inputs'])
            print("Program exited due to error: -1")
            exit(-1)
    
    return linked_addresses


def get_final_balances(address_set, force_local=cached_results):
    '''
    Returns JSON of final balance queries

    Will attempt to get balances from local files if force_local = True
    When querying blockchain.info, 130 addresses per query seems to be the limit
    '''
    baseurl = 'https://blockchain.info/balance?active='

    # This will sum the final balances from local cached results
    if force_local:
        json_response = {}
        if debug:
            print("Summing balances from local cache..")
        for address in address_set:
            incomplete = False
            local_filename = "test_data/" + address + ".json"
            if path.exists(local_filename):
                with open(local_filename) as file:
                    address_response = json.load(file)
                json_response[address] = {'final_balance': address_response['final_balance']}
            else:
                incomplete = True
        if incomplete:
            print("Warning: Incomplete balance due to some addresses not being cached on filesystem. Try online search?")
    # Queries blockchain.info directly for balances
    else:
        if debug:
            print("Querying balances..")
        # Does not work for 130+ addresses with single query, so may need to split
        if len(address_set) < 130:
            query = "|".join(address_set)
            time.sleep(sleep_time)
            r = requests.get(baseurl+query, headers=headers)
            json_response = json.loads(r.text)
        else:
            address_list = list(address_set)
            chunks = [address_list[x:x+130] for x in range(0, len(address_list), 130)]
            if debug:
                print("Estimated time: " + str(len(chunks) * sleep_time / 60) + " Minutes")
            json_response = {}
            for chunk in chunks:
                query = "|".join(chunk)

                time.sleep(sleep_time)
                r = requests.get(baseurl+query, headers=headers)
                partial_response = json.loads(r.text)
                try: # Merge dictionaries - Python 3.5+
                    json_response = {**json_response, **partial_response}
                except: # Using older Python like a pleb
                    print("Warning: Incomplete balance due to old Python version")
                    return json_response

    return json_response


def print_balances(balance_json, print_all=debug):
    ''' Prints balance information passed from the get_final_balances function'''
    total = []
    for key, value in balance_json.items():
        if print_all and len(balance_json.items()) < 50:
            print(str(key) + "\t " + str(value['final_balance']))
        total.append(int(value['final_balance']))
    print("Balance for all linked address:\t\t", sum(total) / 100000000, "BTC (", sum(total), "Satoshis)")


def ensure_dir(file_path):
    ''' Ensures that a directory exists on the local filesystem '''
    directory = path.dirname(file_path)
    if not path.exists(directory):
        makedirs(directory)


def main(address, recursive=recursive, depth_limit=depth_limit):
    '''
    Finds addresses with shared spending to a given address

    May limit the depth of searching 
    '''
    checked_addresses = set()
    to_check = set()

    ensure_dir('./test_data')

    # First pass for linked addresses
    linked_addresses = find_shared_spending(address)

    depth = 1
    if recursive:
        checked_addresses.add(address)
        to_check = linked_addresses - checked_addresses

        # Loop will only break when all linked addresses have been checked
        while len(to_check) > 0:
            if depth_limit:
                if depth >= depth_limit:
                    break

            for linked_address in to_check:
                new_linked_addresses = find_shared_spending(linked_address)

                # Add newly discovered linked addresses to set
                linked_addresses.update(new_linked_addresses)
                # Do not check address again
                checked_addresses.add(linked_address)

            to_check = linked_addresses - checked_addresses
            depth += 1

    print("Results for address:\t\t\t", address)
    print("Total linked addresses:\t\t\t", len(linked_addresses))
    print("Depth:\t\t\t\t\t", depth)

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
