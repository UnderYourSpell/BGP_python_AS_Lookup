import ipaddress
import sys
import urllib3
import requests

urllib3.disable_warnings()

def ipaddress_check(input_ip):
    """Using ipaddress library to validate a IPv4/IPv6 is being provided"""
    #input_ip = input('Please provide IPv4 or IPv6 Public IP address to run search against: ')
    try:
        ip_check = ipaddress.ip_address(input_ip)
        print('%s is a correct IP%s address.' % (ip_check, ip_check.version))
        print('Proceeding with gathering API Data\n')
        return input_ip
    except ValueError:
        print('\nAddress is invalid: %s' % input_ip)
        print('Exiting code, please retry with a valid IPv4 or IPv6 address')
        sys.exit()

def bgp_ip_lookup(ip_addres):
    """Function to lookup a specific IP"""
    response = requests.get('https://api.bgpview.io/ip/' + str(ip_addres))
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        pass
    else:
        res_dict = None
    return res_dict