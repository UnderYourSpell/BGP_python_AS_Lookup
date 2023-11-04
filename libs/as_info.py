from libs import as_api

class ASInfo():
    def __init__(self,asn) -> None:
        self.asn = asn
        self.ip = '0.0.0.0'
        self.peers = as_api.peers(self.asn)
        self.upstreams = as_api.upstream(self.asn)
        self.downstreams = as_api.downstream(self.asn)
        self.as_prefixes = as_api.as_prefixes(self.asn)
        self.details = as_api.details(self.asn)
        self.ixs = as_api.ixs(self.asn)

    def set_asn(self,asn):
        self.asn = asn

    def print_peers(self,v6 = False):
        asn_peers = self.peers
        #asn = int(input("Enter ASN: "))
        #asn_peers = as_api.peers(asn)
        num_peers_v4 = len(asn_peers['data']['ipv4_peers'])
        peer_string_text = ""
        peer_string_text += '\n' + str(self.details['data']['name']) + '\n'
        peer_string_text += str(num_peers_v4) + ' ipv4 peers \n'
        #print(f"\n{num_peers_v4} ipv4 peers: ")
        for peer in range(num_peers_v4):
            isp = asn_peers['data']['ipv4_peers'][peer]['name']
            isp_asnum = asn_peers['data']['ipv4_peers'][peer]['asn']
            peer_string_text += '\n' + str(isp) + ' AS#: ' + str(isp_asnum)
            #print(str(isp) + ' AS#: ' + str(isp_asnum))
        
    
        if v6 == True:
            #could maybe make this optional
            num_peers_v6 = len(asn_peers['data']['ipv6_peers'])

            print(f"\n{num_peers_v6} ipv6 peers: ")
            for peer in range(num_peers_v6):
                isp = asn_peers['data']['ipv6_peers'][peer]['name']
                isp_asnum = asn_peers['data']['ipv6_peers'][peer]['asn']
                print(str(isp) + ' AS#: ' + str(isp_asnum))

        return peer_string_text

    def print_ixs(self):
        asn_ixs = self.ixs
        ixs = len(asn_ixs['data'])
        ix_text = ""
        
        ix_text += '\n' + str(self.details['data']['name']) +' is at ' + str(ixs) +  ' Internet Exchange Points: ' + '\n'

        #print(f"\n{ixs} Internet Exchange Points: ")
        for ix in range(ixs):
            ix_name = asn_ixs['data'][ix]['name']
            ix_id = asn_ixs['data'][ix]['ix_id']
            ix_city = asn_ixs['data'][ix]['city']
            ix_country = asn_ixs['data'][ix]['country_code']
            #ix_speed = asn_ixs['data'][ix]['speed']
            ix_text += '\n' + str(ix_name) + ' '+ str(ix_id) + ' '+ str(ix_city) + ', ' + str(ix_country)
            #print(str(ix_name) + ' with ix id: ' + str(ix_id))
        
        return ix_text

    def print_upstreams(self,v6 = False):
        asn_upstreams = self.upstreams
        len_up = len(asn_upstreams['data']['ipv4_upstreams'])
        up_string_text = ""
        up_string_text += '\n' + str(self.details['data']['name']) + '\n'
        up_string_text += str(len_up) + ' ipv4 upstreams \n'
        #print(f"\n{len_up} IPv4 Upstream ASes: ")
        for peer in range(len_up):
            peer_name = asn_upstreams['data']['ipv4_upstreams'][peer]['name']
            as_num = asn_upstreams['data']['ipv4_upstreams'][peer]['asn']
            up_string_text += '\n' + str(peer_name) + ' AS#: ' + str(as_num)
            #print(str(peer_name) + ' AS#: ' + str(as_num))
        
        if v6 == True:
            len_up = len(asn_upstreams['data']['ipv6_upstreams'])

            print(f"\n{len_up} IPv6 Upstream ASes: ")
            for peer in range(len_up):
                peer_name = asn_upstreams['data']['ipv6_upstreams'][peer]['name']
                as_num = asn_upstreams['data']['ipv6_upstreams'][peer]['asn']
                print(str(peer_name) + ' AS#: ' + str(as_num))

        return up_string_text

    def retrieve_upstream_graphs(self):
        #api gives us a link to a graph
        #this method will give this to us
        pass

    def print_downstreams(self,v6=False):
        asn_downstreams = self.downstreams
        len_up = len(asn_downstreams['data']['ipv4_downstreams'])
        down_string_text = ""
        down_string_text += '\n' + str(self.details['data']['name']) + '\n'
        down_string_text += str(len_up) + ' ipv4 downstreams \n'
        #print(f"\n{len_up} IPv4 Upstream ASes: ")
        for peer in range(len_up):
            peer_name = asn_downstreams['data']['ipv4_downstreams'][peer]['name']
            as_num = asn_downstreams['data']['ipv4_downstreams'][peer]['asn']
            down_string_text += '\n' + str(peer_name) + ' AS#: ' + str(as_num)
            #print(str(peer_name) + ' AS#: ' + str(as_num))
        
        if v6 == True:
            len_up = len(asn_downstreams['data']['ipv6_downstreams'])

            print(f"\n{len_up} IPv6 Upstream ASes: ")
            for peer in range(len_up):
                peer_name = asn_downstreams['data']['ipv6_downstreams'][peer]['name']
                as_num = asn_downstreams['data']['ipv6_downstreams'][peer]['asn']
                print(str(peer_name) + ' AS#: ' + str(as_num))

        return down_string_text

    def print_details(self):
        details = self.details
        out_str = ""
        out_str += 'ASN: ' + str(details['data']['asn']) + '\n'
        out_str += 'Name: ' + str(details['data']['name']) + '\n'
        out_str += 'Description: ' + str(details['data']['description_short']) + '\n'
        out_str += 'Country: ' + str(details['data']['country_code']) + '\n'
        out_str += 'Website: ' + str(details['data']['website']) + '\n'
        out_str += 'looking glass: ' + str(details['data']['looking_glass']) + '\n'
        out_str += 'Traffic Estimation: ' + str(details['data']['traffic_estimation']) + '\n'
        out_str += 'Traffic Ratio: ' + str(details['data']['traffic_ratio']) + '\n'

        return out_str