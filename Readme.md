# Shared Spending Address Finder

This program finds BTC addresses with shared spending and outputs balances of all shared addresses

Uses API from Blockchain.info

Created by: Arghya Mukherjee and Codi West

## Running the program with Python 3

Use the `BlockchainP1_py3.py` file

Run with:

```bash
python BlockchainP1_py3.py
```

Settings:

* Set global settings near the top of the file
* Set BTC address list to check at the bottom of the file

## Running the program with Python 2

Use the `BlockchainP1_py3.py` file

Run with:

```bash
python BlockchainP1v4.py
```

Settings:

* Set BTC address list to check at the top of the file

<div class="page"/>

## Results (from Python 3 version)

As shown in `results` folder

```txt
Results for address:                 15hzoz4YzGnj9Pqu8eNmhw4tBpDGjNgwj9
Total linked addresses:              41475
Depth:                               2
Querying balances..
Too many addresses to display..
Balance for all linked address:      563.23664321 BTC (56323664321 Satoshis)
```

```txt
Results for address:                 36bt43aDDvsMJRd48YiRh6LLrNm3qnGZW5
Total linked addresses:              2
Depth:                               2
Summing balances from local cache..
3Lr3uJY4cHM8zg8WhoLp9pfrsBXAQEj5ao   0
36bt43aDDvsMJRd48YiRh6LLrNm3qnGZW5   0
Balance for all linked address:      0.0 BTC ( 0 Satoshis)
```

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
Balance for all linked address:      0.01459915 BTC ( 1459915 Satoshis)
```

<div class="page"/>

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
Balance for all linked address:      0.01459915 BTC ( 1459915 Satoshis)
```
