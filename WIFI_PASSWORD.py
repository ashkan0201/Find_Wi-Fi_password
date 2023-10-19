import os
import re
from time import sleep as S
from tabulate import tabulate as TB
from getpass import getpass as GP

def WIFI_PASSWORD():
    for INDEX in range(4):
        print(f"\rPlease wait: ({3 - INDEX})", end = '')
        S(1)
    print("\n")

    CODE_RUNNER_1 = os.popen("netsh wlan show profile").readlines()[9:-1]
    MAGIC_LIST_1 = []
    for INDEX in range(len(CODE_RUNNER_1)):
        MAGIC_LIST_1.append(CODE_RUNNER_1[INDEX][27:])

    LIST_JOIN_1 = "".join(MAGIC_LIST_1)
    SPLITER_1 = LIST_JOIN_1.split('\n')
    SPLITER_1.pop()

    MAGIC_LIST_2 = []
    for NAME in SPLITER_1:
        CODE_RUNNER_2 = os.popen(f"netsh wlan show profile name = \"{NAME}\" key = clear").readlines()
        LIST_JOIN_2 = "".join(CODE_RUNNER_2)
        RE_1 = re.findall(pattern = "    Key Content            : .+", string = LIST_JOIN_2)
        SPLITER_2 = RE_1[0].split(":")
        MAGIC_LIST_2.append(SPLITER_2[1])

    print(TB({"NAME" : MAGIC_LIST_1, "PASSWORD" : MAGIC_LIST_2}, headers = "keys", tablefmt = "outline"))
    PRESS_ENTER_TO_FINIFSH = GP("\n<<< PRESS ENTER TO FINIFSH >>>")

if __name__ == "__main__":
    WIFI_PASSWORD()
