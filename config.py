class ChainId:
    ETHEREUM = 1
    BSC = 56
    AVALANCHE = 43114

API_KEY = {
    ChainId.ETHEREUM: "",
    ChainId.BSC: "",
    ChainId.AVALANCHE: ""
}

BROWSER_URL = {
    ChainId.ETHEREUM: "https://etherscan.io",
    ChainId.BSC: "https://bscscan.com",
    ChainId.AVALANCHE: "https://snowtrace.io"
}

GET_SOURCE_CODE_URL = {
    ChainId.ETHEREUM: f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={{}}&apikey={API_KEY[ChainId.ETHEREUM]}",
    ChainId.BSC: f"https://api.bscscan.com/api?module=contract&action=getsourcecode&address={{}}&apikey={API_KEY[ChainId.BSC]}",
    ChainId.AVALANCHE: f"https://api.snowtrace.io/api?module=contract&action=getsourcecode&address={{}}&apikey={API_KEY[ChainId.AVALANCHE]}"
}

RPC_URL = {
    ChainId.ETHEREUM: "https://rpc.flashbots.net",
    ChainId.BSC: "https://bsc-dataseed.binance.org/",
    ChainId.AVALANCHE: "https://api.avax.network/ext/bc/C/rpc"
}


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
