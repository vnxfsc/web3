import requests
import json
from datetime import datetime
import time

first_request_data = None
address = "TFy8LcnqHDUrEZxM3iKZeVC6jgw4XQmmt4"

def print_transaction_data(transactions, message):
    print(message)
    for transaction in transactions:
        txId = transaction['txId']
        transactionTime = int(transaction['transactionTime'])
        transactionTime = datetime.fromtimestamp(transactionTime / 1000).strftime('%Y-%m-%d %H:%M:%S')
        from_address = transaction['from']
        to_address = transaction['to']
        amount = transaction['amount']
        symbol = transaction['symbol']

        print(f"哈希: {txId}")
        print(f"时间: {transactionTime}")
        print(f"来自: {from_address}")
        print(f"收到: {to_address}")
        print(f"金额: {amount} {symbol}")
        print("-" * 50)


while True:
    url = f"https://www.oklink.com/api/v5/explorer/address/token-transaction-list?chainShortName=TRON&address={address}&protocolType=token_20&limit=1"
    headers = {
        'Ok-Access-Key': 'oklink官网申请'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if 'data' in data and 'transactionList' in data['data'][0]:
            transactions = data['data'][0]['transactionList']

            current_data_str = json.dumps(data, ensure_ascii=False)

            if first_request_data is None:
                first_request_data = current_data_str
                print_transaction_data(transactions, "最近交易数据：")
            elif current_data_str != first_request_data:
                print_transaction_data(transactions, "新交易：")
                first_request_data = current_data_str
            else:
                pass
        else:
            print("没有数据.")
    else:
        print(f"HTTP错误码: {response.status_code}")

    time.sleep(5)
