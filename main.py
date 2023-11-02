import as_api
import ip_parse
from as_info import ASInfo

def main():
    asn = ASInfo()
    asn.print_peers(v6 = False) #optional parameter True to also print v6 peers, default is False
    
    asn_ixs = asn.ixs
    ixs = len(asn_ixs['data'])

    print("\n\nAs at Internet Exchange Points: ")
    for ix in range(ixs):
        ix_name = asn_ixs['data'][ix]['name']
        ix_id = asn_ixs['data'][ix]['ix_id']
        print(str(ix_name) + ' with ix id: ' + str(ix_id))

if __name__ == "__main__":
    main()