# Tik-Tool
Tools specifically designed for WISPs to quickly configure MikroTik devices

# Requirements
Windows OS

python 3.7 or greater

fplib, PyQt5 python modules

Make sure that the tik_tool_rc.py file is in the same directory as the Tik Tool Public.py file.

# Setup
The Mikrotik device needs to be reachable via 192.168.88.1.

The tool only knows admin as the user.

The program only knows the blank password or the password that you set on line #482

# Customize
Change line #482 to the password that you want the device to have

Change line #483 to the ROMON seceret that you want the device to have

# Notes
Currently there is only a config for the RB2011, I will be adding other devices and configs later. If you know what you are doing, there are already placeholders for an RB2011 and HAP ac3.

This tool was built with my WISP preferences in mind, feel free to change it to how you would like it.

When you use the firmware upgrade function, the program freezes up while the file is uploading to the device, I will fix that at a later date.

This tool will create a directory under your C:\ drive called Tik-Configs. This is where all of the files are created so that they can be sent via FTP to the device.

Unless you are trying to change things in the actual GUI, you shouldnt have to mess with anything above line #433.

# Customization Help
If you would like for me to customize this tool for you, reach out to me and we can see if we can come to some sort of an agreement. You can find me on the WISP Talk Facebook group - Chris Josey
