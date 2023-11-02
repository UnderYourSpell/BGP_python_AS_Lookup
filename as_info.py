import as_api

class ASInfo():
    def __init__(self) -> None:
        self.asn = input("Enter ASN: ")
        self.ip = '0.0.0.0'
        self.peers = as_api.peers(self.asn)
        self.upstreams = as_api.upstream(self.asn)
        self.downstreams = as_api.downstream(self.asn)
        self.as_prefixes = as_api.as_prefixes(self.asn)
        self.details = as_api.details(self.asn)
        self.ixs = as_api.ixs(self.asn)

    def print_peers(self,v6 = False):
        asn_peers = self.peers
        #asn = int(input("Enter ASN: "))
        #asn_peers = as_api.peers(asn)
        num_peers_v4 = len(asn_peers['data']['ipv4_peers'])

        print("\nipv4 peers: ")
        for peer in range(num_peers_v4):
            isp = asn_peers['data']['ipv4_peers'][peer]['name']
            isp_asnum = asn_peers['data']['ipv4_peers'][peer]['asn']
            print(str(isp) + ' AS#: ' + str(isp_asnum))
        
        if v6 == True:
            #could maybe make this optional
            num_peers_v6 = len(asn_peers['data']['ipv6_peers'])

            print("\nipv6 peers: ")
            for peer in range(num_peers_v6):
                isp = asn_peers['data']['ipv6_peers'][peer]['name']
                isp_asnum = asn_peers['data']['ipv6_peers'][peer]['asn']
                print(str(isp) + ' AS#: ' + str(isp_asnum))
