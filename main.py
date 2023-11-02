import as_api
import ip_parse
from as_info import ASInfo

def main():
    asn = ASInfo()
    asn.print_peers(v6 = False) #optional parameter True to also print v6 peers, default is False
    asn.print_ixs()
   
if __name__ == "__main__":
    main()