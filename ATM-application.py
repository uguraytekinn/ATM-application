accountA = {
    'name': 'Aaron',
    'surname': 'Edgar',
    'accountNo': '26758-24',
    'balance': 2000,
    'sideAccount': 1500
    
}

accountB = {
    'name': 'Thomas',
    'surname': 'Michaelson',
    'accountNo': '56234-12',
    'balance': 3000,
    'sideAccount': 1000

}

def withdrawMoney(account,balance):
    print(f"Welcome {account['name']}")

    if (account['balance'] >= balance):
        account['balance'] -= balance
        print('You can get your money.')
        
    else:
        total = account['balance'] + account['sideAccount']

        if (total >= balance):
             sideAccountUsage = input("Use additional account ?(y/n)")

             if sideAccountUsage == 'y':
                 sideAccountUse = balance - account['balance']
                 account['balance'] = 0
                 account['sideAccount'] -= sideAccountUse
                 print('You can get your money.')
                 balanceInquiry(account)
             else:
                print(f"{account['accountNo']} in your account no {account['balance']} remaining amount")
        else:
            print("There is insufficient money in your account.")
            balanceInquiry(account)


def balanceInquiry(account):
    print(f"{account['accountNo']} in your account no {account['balance']} USD there is. Your additional account limit is {account['sideAccount']} USD there is.")

withdrawMoney(accountA, 1800)
balanceInquiry(accountA)