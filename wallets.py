from web3.auto import w3


def generate_wallet():
    account = w3.eth.account.create()
    return account.address, account._private_key.hex()


num_wallets = int(input("请输入要生成几个钱包: "))
with open("wallets.txt", "w", encoding="utf-8") as file:
    for _ in range(num_wallets):
        address, private_key = generate_wallet()
        file.write(f"地址: {address}\n")
        file.write(f"私钥: {private_key}\n\n")

print(f"已生成 {num_wallets} 个钱包，并保存到 wallets.txt 文件中。")
