from libs.as_info import ASInfo
from libs import ip
from tkinter import *
from tkinter.ttk import *
import tkinter.font as font

#from tkinter_functions import display_peers
   
# writing code needs to
# create the main window of 
# the application creating 
# main window object named root
root = Tk()
#root['background']='grey'##856ff8
myFont = font.Font(family='Courier')
# giving title to the main window
root.title("AS Information")
root.geometry('720x460')


#target_asn = StringVar()
as_entry_label = Label(root,text= "Enter ASN:")
as_entry_label.grid(column=1,row=1,sticky='ew')
as_entry = Entry(root)
as_entry.grid(column= 2, row = 1,sticky='ew')

ip_entry_label = Label(root,text = "Get ASN from IP address: ")
ip_entry_label.grid(column = 4, row = 1,sticky='ew')
ip_entry = Entry(root)
ip_entry.grid(column=5, row = 1,sticky='ew')

def ip_enter_clicked():
    text_display.delete("1.0", "end")
    if ip_entry.get() == "":
        text_display.insert("end", "No IP address entered")
    else:
        ip_entered = ip_entry.get()
        ip_address = ip.ipaddress_check(ip_entered)
        ip_data = ip.bgp_ip_lookup(ip_address)
        asn = ip_data['data']['prefixes'][0]['asn']['asn']
        display_text = 'ASN: ' + str(asn)
        text_display.insert("end", display_text)


ip_enter_btn = Button(root,text = "Enter",command = ip_enter_clicked)
ip_enter_btn.grid(column=6, row = 1,sticky='ew')



asns = [123,1222,333]
as_info_objects = []
# function to display user text when
# button is clicked
def enter_clicked():
    new_asn = int(as_entry.get())
    new_asn_object = ASInfo(new_asn)
    as_info_objects.append(new_asn_object)
    asns.append(new_asn)
# button widget with red color text inside
enter_btn = Button(root, text = "Enter" , command=enter_clicked)
# Set Button Grid
enter_btn.grid(column=3, row=1,sticky='ew')

def display_peers():
    text_display.delete("1.0", "end")
    if as_info_objects:
        asn = as_info_objects[-1]  # Get the last entered ASN
        # Display the relevant information based on the ASN
        display_text = f"Displaying peers for ASN {asn.asn}\n"
        display_text += asn.print_peers()
        text_display.insert("end", display_text)
    else:
        text_display.insert("end", "No ASN entered yet.\n")
        #print(f"Displaying peers for ASN {asn.asn}")
        #asn.print_peers()

def display_upstreams():
    text_display.delete("1.0", "end")
    if as_info_objects:
        asn = as_info_objects[-1]  # Get the last entered ASN
        # Display the relevant information based on the ASN
        display_text = f"Displaying upstreams for ASN {asn.asn}\n"
        display_text += asn.print_upstreams()
        text_display.insert("end", display_text)
    else:
        text_display.insert("end", "No ASN entered yet.\n")

def display_downstreams():
    text_display.delete("1.0", "end")
    if as_info_objects:
        asn = as_info_objects[-1]  # Get the last entered ASN
        # Display the relevant information based on the ASN
        display_text = f"Displaying downstreams for ASN {asn.asn}\n"
        display_text += asn.print_downstreams()
        text_display.insert("end", display_text)
    else:
        text_display.insert("end", "No ASN entered yet.\n")

def display_ixs():
    text_display.delete("1.0", "end")
    if as_info_objects:
        asn = as_info_objects[-1]  # Get the last entered ASN
        # Display the relevant information based on the ASN
        display_text = f"Displaying IXPs for ASN {asn.asn}\n"
        display_text += asn.print_ixs()
        text_display.insert("end", display_text)
    else:
        text_display.insert("end", "No ASN entered yet.\n")

def display_details():
    text_display.delete("1.0", "end")
    if as_info_objects:
        asn = as_info_objects[-1]
        display_text = asn.print_details()
        text_display.insert("end",display_text)
    else:
        text_display.insert("end", "No ASN entered yet.\n")

#display_details_btn = Button(root,text="Display ASN Details",command = display_details)
#display_details_btn.grid(column=1,row=2)

display_peers_btn = Button(root,text="Display Peers",command = display_peers)
display_peers_btn.grid(column=2,row=2,sticky='ew')

display_upstreams_btn = Button(root,text="Display Upstreams",command = display_upstreams)
display_upstreams_btn.grid(column=3,row=2,sticky='ew')

display_downstreams_btn = Button(root,text="Display Downstreams",command = display_downstreams)
display_downstreams_btn.grid(column=4,row=2,sticky='ew')

display_ixs_btn = Button(root,text="Display IXP's",command = display_ixs)
display_ixs_btn.grid(column=5,row=2,sticky='ew')

display_details_btn = Button(root,text="Display Details",command = display_details)
display_details_btn.grid(column=1,row=2,sticky='ew')

#need a display details button

text_display = Text(root)
text_display.grid(column = 1,row=7,columnspan=5,sticky='w')




root.mainloop()
