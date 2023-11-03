from as_info import ASInfo
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo

#from tkinter_functions import display_peers
   
# writing code needs to
# create the main window of 
# the application creating 
# main window object named root
root = Tk()

#menu
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)
# giving title to the main window
root.title("AS Information")
root.geometry('980x530')


#target_asn = StringVar()
as_entry_label = Label(root,text= "Enter ASN")
as_entry_label.grid(column=1,row=1)
as_entry = Entry(root)
as_entry.grid(column= 2, row = 1)

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
btn1 = Button(root, text = "Enter" , command=enter_clicked)
# Set Button Grid
btn1.grid(column=3, row=1)

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
    if as_info_objects:
        asn = as_info_objects[-1]  # Get the last entered ASN
        # Display the relevant information based on the ASN
        print(f"Displaying upstreams for ASN {asn.asn}")
        asn.print_upstreams()
    else:
        print("No ASN entered yet.")

def display_downstreams():
    if as_info_objects:
        asn = as_info_objects[-1]  # Get the last entered ASN
        # Display the relevant information based on the ASN
        print(f"Displaying downstreams for ASN {asn.asn}")
        asn.print_downstreams()
    else:
        print("No ASN entered yet.")

def display_ixs():
    if as_info_objects:
        asn = as_info_objects[-1]  # Get the last entered ASN
        # Display the relevant information based on the ASN
        print(f"Displaying IXPs for ASN {asn.asn}")
        asn.print_ixs()
    else:
        print("No ASN entered yet.")

#display_details_btn = Button(root,text="Display ASN Details",command = display_details)
#display_details_btn.grid(column=1,row=2)

display_peers_btn = Button(root,text="Display Peers",command = display_peers)
display_peers_btn.grid(column=1,row=2)

display_upstreams_btn = Button(root,text="Display Upstreams",command = display_upstreams)
display_upstreams_btn.grid(column=1,row=3)

display_downstreams_btn = Button(root,text="Display Downstreams",command = display_downstreams)
display_downstreams_btn.grid(column=1,row=4)

display_ixs_btn = Button(root,text="Display IXP's",command = display_ixs)
display_ixs_btn.grid(column=1,row=5)

text_display = Text(root)
text_display.grid(column = 4,row=6)




root.mainloop()
