#! /usr/bin/python3
from config import *
import sys, re, requests, json, os, shutil

def importReplace(matched):
    return "import \"./" + os.path.basename(matched.group('filename')) + "\"";

def preCheck():
    global contract_address

    if (len(sys.argv) != 2):
        sys.exit(bcolors.FAIL + "Usage: soc <URL>" + bcolors.ENDC)

    res = re.findall(r'.*([0-9a-zA-Z]{40}).*', sys.argv[1])

    if (len(res) != 1):
        sys.exit(bcolors.FAIL + "Confused about given URL or address" + bcolors.ENDC)

    contract_address = "0x" + res[0]


def work():
    print( "Searching solidity code of address:", bcolors.OKGREEN , contract_address, bcolors.ENDC)
    res = requests.get(ETHERSCAN_MAINNET_GET_SOURCE_CODE_URL.format(contract_address)).json()

    contract_name = res['result'][0]['ContractName']

    base_dir = os.path.join(os.getcwd(), "contracts", contract_name)
    print("Creating directory:", bcolors.OKBLUE, base_dir, bcolors.ENDC)
    while os.path.exists(base_dir):
        c = input(f"source file direct already exists, replace it, save as another name or {bcolors.WARNING}cancel{bcolors.ENDC}?(r/s/{bcolors.WARNING}C{bcolors.ENDC})")
        if c == 'r':
            shutil.rmtree(base_dir)
        elif c == 's':
            base_dir = base_dir + "_1"
            print("Creating directory:", bcolors.OKBLUE, base_dir, bcolors.ENDC)
        else:
            sys.exit(bcolors.FAIL + "cancel" + bcolors.ENDC)

    os.makedirs(base_dir)

    codes = res['result'][0]['SourceCode']
    if (codes[0] == '{' and codes[1] == '{'):
        codes = json.loads(codes[1:-1])['sources']
        for i in codes:
            raw_code = codes[i]['content']
            data = re.sub(r".*import.*['\"](?P<filename>.*\.sol)['\"]", importReplace, raw_code)

            filename = os.path.join(base_dir, os.path.basename(i))
            print("Writing file:", bcolors.OKBLUE, filename, bcolors.ENDC)
            with open(filename, "w") as f:
                f.write(data) 
    else:
        filename = os.path.join(base_dir, res['result'][0]['ContractName'] + ".sol")
        print("Writing file:", bcolors.OKBLUE, filename, bcolors.ENDC)
        with open(filename, "w") as f:
            f.write(codes)
        

def main():
    preCheck()
    work()

if __name__ == "__main__":
    main()
