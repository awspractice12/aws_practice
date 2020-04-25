import subprocess
import sys
import time
import os
from tempfile import mkstemp
from shutil import move
from aws import aws_conf

#=======================================
#	Main Program
#=======================================
if __name__ == "__main__":

    # aws_conf.ec2_cr8_keypair('test','test.pem')
    aws_conf.ec2_dl8_keypair('test')
    sys.exit(0)
	#=====================
	#Parse arguments
	#=====================
    profile_name = " "
    x = 0
    while x < len(sys.argv):
        if sys.argv[x] == "--help":
            mode = "help"
        elif sys.argv[x] == "--profile":
            mode = "profile"
            x=x+1
            if x < len(sys.argv):
                profile_name =str(sys.argv[x])
        else:
            mode = "profile"
        x=x+1	

	#==============================================================
	#Execute the script based on mode determined through arguments
	#==============================================================
    if mode == "help":
        aws_conf.usage()
    elif mode == "profile":
        aws_conf.configure_awscli(profile_name)