import ipaddress as ip
import sys
import urllib3
import requests
urllib3.disable_warnings()



#function to retrieve
def as_prefixes(asn):
    """Function to find ISPs"""
    response = requests.get('https://api.bgpview.io/asn/' + str(asn) +'/prefixes')
    #Convert Response to JSON/Dictionary to read/view data better
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        pass
    else:
        res_dict = None
    return res_dict
    pass

def details(asn):
    '''Details of AS'''
    response = requests.get("https://api.bgpview.io/asn/" + str(asn))
    res_dict = response.json()

    if res_dict['status'] == 'ok':
        #store certain types of data into different lists
        pass
    else:
        res_dict = None
    return res_dict

def peers(asn):
    """Function to identify what ISP are peer'd with source ASN#"""
    response = requests.get('https://api.bgpview.io/asn/' + str(asn) +'/peers')
    #Convert Response to JSON/Dictionary to read/view data better
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        pass
    else:
        res_dict = None
    return res_dict

def upstream(asn):
    """Function to find ISPs upstream"""
    response = requests.get('https://api.bgpview.io/asn/' + str(asn) +'/upstreams')
    #Convert Response to JSON/Dictionary to read/view data better
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        pass
    else:
        res_dict = None
    return res_dict

def downstream(asn):
    """Function to find ISPs downstream"""
    response = requests.get('https://api.bgpview.io/asn/' + str(asn) +'/downstreams')
    #Convert Response to JSON/Dictionary to read/view data better
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        pass
    else:
        res_dict = None
    return res_dict
    

def ixs(asn):
    """Function to find IXs that the ASN is at"""
    response = requests.get('https://api.bgpview.io/asn/' + str(asn) +'/ixs')
    #Convert Response to JSON/Dictionary to read/view data better
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        pass
    else:
        res_dict = None
    return res_dict

def ip_prefixes(asn):
    pass

def retrieve_asn(asn):
    pass

    