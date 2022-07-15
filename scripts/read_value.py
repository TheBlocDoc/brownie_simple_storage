from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
    # next, take the index thats one less than the length
    # ABI
    # ADDRESS
