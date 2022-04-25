class ChainId:
    ETHEREUM = 1
    BSC = 56
    AVALANCHE = 43114
    POLYGON = 137

API_KEY = {
    ChainId.ETHEREUM: "",
    ChainId.BSC: "",
    ChainId.AVALANCHE: "",
    ChainId.POLYGON: "",
}

BROWSER_URL = {
    ChainId.ETHEREUM: "etherscan.io",
    ChainId.BSC: "bscscan.com",
    ChainId.AVALANCHE: "snowtrace.io",
    ChainId.POLYGON: "polygonscan.com"
}

RPC_URL = {
    ChainId.ETHEREUM: "https://rpc.flashbots.net",
    ChainId.BSC: "https://bsc-dataseed.binance.org/",
    ChainId.AVALANCHE: "https://api.avax.network/ext/bc/C/rpc",
    ChainId.POLYGON: "https://polygon-rpc.com/"
}

RPC_ENDPOINTS = {
    "getsourcecode": "https://api.{}/api?module=contract&action=getsourcecode&address={}&apikey={}"
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
