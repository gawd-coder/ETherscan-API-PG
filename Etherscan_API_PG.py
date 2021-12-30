import requests

my_address = "0x1844cc9d499d934271438a193561671a1d7ef5e1"
my_multiple_address = "0x1844cc9d499d934271438a193561671a1d7ef5e1,0xa8f9c1dc37fc800c251c4780961794771b08621a"
YourApiKeyToken = "R3P366TKNI9ETATACNYWDS868D5V4DTDZJ"
 
# Get Ether Balance for a Single Address
x = requests.get(
   "https://api.etherscan.io/api?module=account&action=balance&address="+my_address+\
   "&tag=latest&apikey="+YourApiKeyToken
)
 
x = x.json()
 
# print("ETH balance of given wallet is {} ETH".format(int(x['result']) / 10**18))
# {'status': '1', 'message': 'OK', 'result': '336674612752397999'}

# Get Ether Balance for Mutiple Address
x = requests.get(
   "https://api.etherscan.io/api?module=account&action=balancemulti&address="+my_multiple_address+\
   "&tag=latest&apikey="+YourApiKeyToken
)
 
x = x.json()

# for i in x['result']:
#    print("ETH balance of given wallet {0} is {1} ETH".format(i['account'], int(i['balance']) / 10**18))

# ETH balance of given wallet 0x1844cc9d499d934271438a193561671a1d7ef5e1 is 0.2698455620238869 ETH
# ETH balance of given wallet 0xa8f9c1dc37fc800c251c4780961794771b08621a is 3.6812899409782824 ETH

# Get a list of 'Normal' Transactions By Address
x = requests.get(
   "https://api.etherscan.io/api?module=account&action=txlist&address=" + my_address + \
   "&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=" + YourApiKeyToken
)

x = x.json()

# for i in x['result']:
#    print("\n", i)

# multiple of these:
# {'blockNumber': '11294830', 'timeStamp': '1605873344', 'hash': '0xb4e639d8f9732b9873588d8888467310912fa52af6eb507cc69e5c6f08bc2598', 
# 'nonce': '23832', 'blockHash': '0x3bc5001f37745c6ae5a9dffbb29544214beab7e5f8d9b6785a8b32e5d32050bf', 'transactionIndex': '39', 
# 'from': '0xd897fe50cc3f57ddea02c8c21d5ff3eb03387310', 'to': '0x1844cc9d499d934271438a193561671a1d7ef5e1', 'value': '12877741910000000000', 
# 'gas': '90000', 'gasPrice': '69000000000', 'isError': '0', 'txreceipt_status': '1', 'input': '0x', 'contractAddress': '', 
# 'cumulativeGasUsed': '2163094', 'gasUsed': '21000', 'confirmations': '2606539'}

# Get a list of 'Internal' Transactions by Address
x = requests.get(
   "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + my_address + \
   "&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=" + YourApiKeyToken
)

x = x.json()

# for i in x['result']:
#    print("\n", i)

# multiple of these:
# {'blockNumber': '13745595', 'timeStamp': '1638700878', 'hash': '0x2a533304998ed4cb95cfe3320704a3685b4fdb5145c7ea58c1419a67d8624adf', 'from': '0xc310e760778ecbca4c65b6c559874757a4c4ece0', 'to': '0x1844cc9d499d934271438a193561671a1d7ef5e1', 'value': '79000000000000000000', 'contractAddress': '', 'input': '', 'type': 'call', 'gas': '2300', 'gasUsed': '0', 'traceId': '3', 'isError': '0', 'errCode': ''}

# Get 'Internal Transactions' by Transaction Hash: Returns the list of internal transactions performed within a transaction.

x = requests.get(
   "https://api.etherscan.io/api?module=account&action=txlistinternal&txhash=0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170&apikey=" + YourApiKeyToken 
)

x = x.json()

# for i in x['result']:
#    print("\n", i)

# {'blockNumber': '1743059', 'timeStamp': '1466489498', 'from': '0x2cac6e4b11d6b58f6d3c1c9d5fe8faa89f60e5a2', 'to': '0x66a1c3eaf0f1ffc28d209c0763ed0ca614f3b002', 'value': '7106740000000000', 'contractAddress': '', 'input': '', 'type': 'call', 'gas': '2300', 'gasUsed': '0', 'isError': '0', 'errCode': ''}

