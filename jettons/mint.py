from tonsdk.contract.token.ft import JettonMinter, JettonWallet
from tonsdk.utils import Address
from wallet_creation.deploy_wallet import wallet_address

def create_state_init_jetton():
    minter = JettonMinter(admin_address=Address(wallet_address))
