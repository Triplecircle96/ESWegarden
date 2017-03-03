# Class that will execute commands on threads from Slack
# Process this Class goes through
# 1. Object created in Main
# 2. Object will be passed into slack, so that slack can call its methods
# 3. Object will get system thread objects sent into it

from systemTypes import nft
from systemTypes import drip
from systemTypes import ebbnflow

class threadController:
    def __init__(self):
        print("System Thread Manager Created")