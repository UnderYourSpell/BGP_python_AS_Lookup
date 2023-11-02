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

        print(f"\n{num_peers_v4} ipv4 peers: ")
        for peer in range(num_peers_v4):
            isp = asn_peers['data']['ipv4_peers'][peer]['name']
            isp_asnum = asn_peers['data']['ipv4_peers'][peer]['asn']
            print(str(isp) + ' AS#: ' + str(isp_asnum))
        
        if v6 == True:
            #could maybe make this optional
            num_peers_v6 = len(asn_peers['data']['ipv6_peers'])

            print(f"\n{num_peers_v6} ipv6 peers: ")
            for peer in range(num_peers_v6):
                isp = asn_peers['data']['ipv6_peers'][peer]['name']
                isp_asnum = asn_peers['data']['ipv6_peers'][peer]['asn']
                print(str(isp) + ' AS#: ' + str(isp_asnum))

    def print_ixs(self):
        asn_ixs = self.ixs
        ixs = len(asn_ixs['data'])

        print(f"\n{ixs} Internet Exchange Points: ")
        for ix in range(ixs):
            ix_name = asn_ixs['data'][ix]['name']
            ix_id = asn_ixs['data'][ix]['ix_id']
            print(str(ix_name) + ' with ix id: ' + str(ix_id))

    def print_upstreams(self,v6 = False):
        asn_upstreams = self.upstreams
        len_up = len(asn_upstreams['data']['ipv4_upstreams'])

        print(f"\n{len_up} IPv4 Upstream ASes: ")
        for peer in range(len_up):
            peer_name = asn_upstreams['data']['ipv4_supstreams'][peer]['name']
            as_num = ['data']['ipv4_upstreams'][peer]['asn']
            print(str(peer_name) + ' AS#: ' + str(as_num))
        
        if v6 == True:
            len_up = len(asn_upstreams['data']['ipv6_upstreams'])

            print(f"\n{len_up} IPv6 Upstream ASes: ")
            for peer in range(len_up):
                peer_name = asn_upstreams['data']['ipv6_supstreams'][peer]['name']
                as_num = ['data']['ipv6_upstreams'][peer]['asn']
                print(str(peer_name) + ' AS#: ' + str(as_num))


    def retrieve_upstream_graph(self):
        #api gives us a link to a graph
        #this method will give this to us
        pass

    def print_downstreams(self):
        pass