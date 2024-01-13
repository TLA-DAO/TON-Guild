from tonsdk.contract.wallet import Wallets, WalletVersionEnum

# mnemonics, pub_k, priv_k, wallet = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)

mnemonic = ['harsh', 'tilt', 'problem', 'act', 'foam', 'accuse', 'card', 'ride', 'coil', 'moon', 'cattle', 'gaze',
            'outer',
            'bonus', 'office', 'deliver', 'prison', 'brain', 'decline', 'walnut', 'minimum', 'neither', 'valve',
            'divide']

mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonic,
                                                          version=WalletVersionEnum.v3r2,
                                                          workchain=0)

wallet_address = wallet.address.to_string(True, True, True, True)
print(mnemonics)
print(wallet_address)
