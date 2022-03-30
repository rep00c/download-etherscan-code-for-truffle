ETHERSCAN_API_KEY = "FILL IT!"
ETHERSCAN_MAINNET_GET_SOURCE_CODE_URL = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={{}}&apikey={ETHERSCAN_API_KEY}"
ETHEREUM_RPC_URL = "https://rpc.flashbots.net"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
