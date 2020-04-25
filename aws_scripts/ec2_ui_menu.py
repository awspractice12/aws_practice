import tkinter
from tkinter import ttk
import random
from ec2_instance import awsec2 
import main as mn
def main():

    app = tkinter.Tk()
    app.title("Amazon Web Sevices")

    main_frame = ttk.Frame(app, padding=40)
    main_frame.grid()  # only grid call that does NOT need a row and column

    create_button = ttk.Button(main_frame, text="Create Instance")
    create_button.grid()
    create_button['command'] = lambda: mn.main_create_instance()

    delete_button = ttk.Button(main_frame, text="Delete Instance")
    delete_button.grid()
    delete_button['command'] = lambda: mn.main_terminate_instance()

    lists_button = ttk.Button(main_frame, text="List Instances & Public IP's")
    lists_button.grid()
    lists_button['command'] = lambda: awsec2.get_public_ip()

    list_button = ttk.Button(main_frame, text="List Instance / Public IP")
    list_button.grid()
    # list_button['command'] = lambda: awsec2.get_inst_public_ip(instance_id) #-- Not Working Need To Check

    start_button = ttk.Button(main_frame, text="Start Instance")
    start_button.grid()
    action      = "start"
    start_button['command'] = lambda: awsec2.ec2_instance_start_stop("start",'i-0f3120acec1ed16bd')

    stop_button = ttk.Button(main_frame, text="Stop Instance")
    stop_button.grid()
    action      = "stop"
    stop_button['command'] = lambda: awsec2.ec2_instance_start_stop(action,'i-0f3120acec1ed16bd')

    reboot_button = ttk.Button(main_frame, text="Reboot Instance")
    reboot_button.grid()
    # instance_id = 'i-0f3120acec1ed16bd'
    reboot_button['command'] = lambda: awsec2.ec2_instance_reboot('i-0f3120acec1ed16bd')

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid()
    e_button['command'] = lambda: exit()

    app.mainloop()


main()