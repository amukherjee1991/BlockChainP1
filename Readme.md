# Shared Spending Address Finder

This program finds BTC addresses with shared spending and outputs balances of all shared addresses

Uses API from Blockchain.info

Python 2 Version: Arghya Mukherjee

Python 3 Version: Codi West

## Running the program with Python 2

Use the `BlockchainP1_py2_v5.py` file

Run with:

```bash
python BlockchainP1v4.py
```

Settings:

* Set BTC address list to check at the top of the file

## Running the program with Python 3

Use the `BlockchainP1_py3.py` file

Run with:

```bash
python BlockchainP1_py3.py
```

Settings:

* Set global settings near the top of the file
* Set BTC address list to check at the bottom of the file

<div class="page"/>

## Results

As shown in `results` folder

### Large TX Address

Python 3 Version:

```txt
Results for address:                 15hzoz4YzGnj9Pqu8eNmhw4tBpDGjNgwj9
Total linked addresses:              41475
Depth:                               2
Querying balances..
Too many addresses to display..
Balance for all linked address:      563.23664321 BTC (56323664321 Satoshis)
```

### Small TX Address

Python 2 Version:

```txt
#################################################
bitcoin address: 36bt43aDDvsMJRd48YiRh6LLrNm3qnGZW5
#################################################
# of addresses linked with  36bt43aDDvsMJRd48YiRh6LLrNm3qnGZW5 is  2
balance of  36bt43aDDvsMJRd48YiRh6LLrNm3qnGZW5 is: 0.0
balance of  3Lr3uJY4cHM8zg8WhoLp9pfrsBXAQEj5ao is: 0.0
#################################################
Total Balance is: 0.0
#################################################
```

Python 3 Version:

```txt
Results for address:                 36bt43aDDvsMJRd48YiRh6LLrNm3qnGZW5
Total linked addresses:              2
Depth:                               2
Summing balances from local cache..
3Lr3uJY4cHM8zg8WhoLp9pfrsBXAQEj5ao   0
36bt43aDDvsMJRd48YiRh6LLrNm3qnGZW5   0
Balance for all linked address:      0.0 BTC (0 Satoshis)
```

<div class="page"/>

### Dormant 1 Address

Python 2 Version:

```txt
###########################
bitcoin address: 19ere2oJzJh81A5Q64SExDZYz54RvWHqZz
###########################
# of addresses linked with  19ere2oJzJh81A5Q64SExDZYz54RvWHqZz is  16
balance of 19ere2oJzJh81A5Q64SExDZYz54RvWHqZz is 0.0993905
balance of 15g4a2znVdCHehDBYBduZRmTjf1urH2zgU is 0.0
balance of 1JPH9G46QqGSWobb4ZWJZZoydfds6Pgrwt is 0.0052
balance of 1BcR5cmcxfsow8JiBuDjtHRYTNs7g9tSeR is 0.0
balance of 19QDGMRKdZ9BpDZP2Re6yaDqNQ7zN4wo1D is 0.0151
balance of 12wNM39xprrzkUoJ9cQbJMuerKt5iWCZuD is 0.0051
balance of 1A6tSUk1NfEPBLEUBFNXAPwnBR5KiB9zvT is 0.0
balance of 14c8poWuaYvkysSdTCX7P6E5cCXJRsYigK is 0.0
balance of 13uraL1Maba7obbhkdB4pjsqMyvqrcTeeD is 0.016001
balance of 1rqA6iteBVryQV3yjF7DHR3Mew8PhxNV8 is 0.0052
balance of 1GcDdCJBGBGKxqvMzYfYq5ZQs3smUSAfXa is 0.0
balance of 1Kus69tpnTzCwKy7zVLU7f2sDvGDUkiPz5 is 0.0
balance of 1FwEVEYnESzvU5Laj891EvHmDkvdkwY6Vs is 0.0
balance of 17S4oE21kRw51ZpyWQL6CsBaytNphy1Jsz is 0.0
balance of 15wLC2HB6sWAuge98xYpR8AoZdtk5Dg4cL is 0.0
balance of 14jGmpwuKRfChGFqfSma941R2AjwfC4r23 is 0.0
#################################################
Total Balance is: 0.1459915
#################################################
```

<div class="page"/>

Python 3 Version:

```txt
Results for address:                 19ere2oJzJh81A5Q64SExDZYz54RvWHqZz
Total linked addresses:              16
Depth:                               5
Summing balances from local cache..
14c8poWuaYvkysSdTCX7P6E5cCXJRsYigK   0
12wNM39xprrzkUoJ9cQbJMuerKt5iWCZuD   51000
1GcDdCJBGBGKxqvMzYfYq5ZQs3smUSAfXa   0
14jGmpwuKRfChGFqfSma941R2AjwfC4r23   0
1rqA6iteBVryQV3yjF7DHR3Mew8PhxNV8    52000
1A6tSUk1NfEPBLEUBFNXAPwnBR5KiB9zvT   0
1BcR5cmcxfsow8JiBuDjtHRYTNs7g9tSeR   0
19ere2oJzJh81A5Q64SExDZYz54RvWHqZz   993905
15wLC2HB6sWAuge98xYpR8AoZdtk5Dg4cL   0
17S4oE21kRw51ZpyWQL6CsBaytNphy1Jsz   0
15g4a2znVdCHehDBYBduZRmTjf1urH2zgU   0
1FwEVEYnESzvU5Laj891EvHmDkvdkwY6Vs   0
1JPH9G46QqGSWobb4ZWJZZoydfds6Pgrwt   52000
1Kus69tpnTzCwKy7zVLU7f2sDvGDUkiPz5   0
13uraL1Maba7obbhkdB4pjsqMyvqrcTeeD   160010
19QDGMRKdZ9BpDZP2Re6yaDqNQ7zN4wo1D   151000
Balance for all linked address:      0.01459915 BTC (1459915 Satoshis)
```

<div class="page"/>

### Dormant 2 Address

Python 2 Version:

```txt
#################################################
bitcoin address: 19QDGMRKdZ9BpDZP2Re6yaDqNQ7zN4wo1D
#################################################
# of addresses linked with  19QDGMRKdZ9BpDZP2Re6yaDqNQ7zN4wo1D is  16
balance of  13uraL1Maba7obbhkdB4pjsqMyvqrcTeeD is: 0.0016001
balance of  1GcDdCJBGBGKxqvMzYfYq5ZQs3smUSAfXa is: 0.0
balance of  1BcR5cmcxfsow8JiBuDjtHRYTNs7g9tSeR is: 0.0
balance of  1JPH9G46QqGSWobb4ZWJZZoydfds6Pgrwt is: 0.00052
balance of  14jGmpwuKRfChGFqfSma941R2AjwfC4r23 is: 0.0
balance of  15g4a2znVdCHehDBYBduZRmTjf1urH2zgU is: 0.0
balance of  15wLC2HB6sWAuge98xYpR8AoZdtk5Dg4cL is: 0.0
balance of  1A6tSUk1NfEPBLEUBFNXAPwnBR5KiB9zvT is: 0.0
balance of  17S4oE21kRw51ZpyWQL6CsBaytNphy1Jsz is: 0.0
balance of  19ere2oJzJh81A5Q64SExDZYz54RvWHqZz is: 0.00993905
balance of  1Kus69tpnTzCwKy7zVLU7f2sDvGDUkiPz5 is: 0.0
balance of  19QDGMRKdZ9BpDZP2Re6yaDqNQ7zN4wo1D is: 0.00151
balance of  12wNM39xprrzkUoJ9cQbJMuerKt5iWCZuD is: 0.00051
balance of  1FwEVEYnESzvU5Laj891EvHmDkvdkwY6Vs is: 0.0
balance of  1rqA6iteBVryQV3yjF7DHR3Mew8PhxNV8 is: 0.00052
balance of  14c8poWuaYvkysSdTCX7P6E5cCXJRsYigK is: 0.0
#################################################
Total Balance is: 0.01459915
```

<div class="page"/>

Python 3 Version:

```txt
Results for address:                 19QDGMRKdZ9BpDZP2Re6yaDqNQ7zN4wo1D
Total linked addresses:              16
Depth:                               4
Summing balances from local cache..
14c8poWuaYvkysSdTCX7P6E5cCXJRsYigK   0
12wNM39xprrzkUoJ9cQbJMuerKt5iWCZuD   51000
1GcDdCJBGBGKxqvMzYfYq5ZQs3smUSAfXa   0
14jGmpwuKRfChGFqfSma941R2AjwfC4r23   0
1rqA6iteBVryQV3yjF7DHR3Mew8PhxNV8    52000
1A6tSUk1NfEPBLEUBFNXAPwnBR5KiB9zvT   0
1BcR5cmcxfsow8JiBuDjtHRYTNs7g9tSeR   0
19ere2oJzJh81A5Q64SExDZYz54RvWHqZz   993905
15wLC2HB6sWAuge98xYpR8AoZdtk5Dg4cL   0
17S4oE21kRw51ZpyWQL6CsBaytNphy1Jsz   0
15g4a2znVdCHehDBYBduZRmTjf1urH2zgU   0
1FwEVEYnESzvU5Laj891EvHmDkvdkwY6Vs   0
1JPH9G46QqGSWobb4ZWJZZoydfds6Pgrwt   52000
1Kus69tpnTzCwKy7zVLU7f2sDvGDUkiPz5   0
13uraL1Maba7obbhkdB4pjsqMyvqrcTeeD   160010
19QDGMRKdZ9BpDZP2Re6yaDqNQ7zN4wo1D   151000
Balance for all linked address:      0.01459915 BTC (1459915 Satoshis)
```
