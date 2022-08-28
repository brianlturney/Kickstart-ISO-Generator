[![GitHub license](https://img.shields.io/github/license/brianlturney/Rocky-Linux-Kickstart-Image-Generator)](https://github.com/brianlturney/Kickstart-ISO-Generator/blob/main/LICENSE)   ![](https://komarev.com/ghpvc/?username=brianlturney)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Linux Kickstart ISO Generator

# Description

This kickstart image generator is an elegant and fast way to create custom ISOs automatically and securely to allow you to auto-install your favorite  Fedora linux (RHEL, CentOS, Rocky, etc) on hypervisors or bare metal.

Compatible to run on:
- Rocky Linux
- CentOS
- RedHat Enterprise Linux
- Kali
- and many other Fedora distros...

Compatible to customize ISOs for:
- CentOS
- Red Hat Enterprise Linux
- Rocky Linux
- and other Fedora distros...

* This has not been engineered yet to run on Debian, Suse, and other non-Fedora distros.

# Requirements

- Python3

# What it does

1) Download the ISO you select
2) Mount the ISO and extract
3) Update the ISO with the advanced Kickstart auto install parameters
4) Check which distribution you are running and choose the compatible pathway to success
5) Create a BIOS and UEFI hybrid bootable ISO

# Options

By making simple edits to the Kickstart ks.cfg you can enable or disable options such as:
- Drive encryption
- Users and passwords
- Add users to groups
- Create root user and password
- Set user password age minimum
- Set timezone for your part of the world
- Install packages
- Enable/disable services
- Enable/disable automatic security updates
- Hundreds of other options you can add from the Kickstart reference located at
  https://docs.fedoraproject.org/en-US/fedora/latest/install-guide/appendixes/Kickstart_Syntax_Reference/
  
# How to use

- Run 'sudo git clone' for this git url
- Run 'cd Kickstart-IOS-Generator'
- Run 'sudo chmod +x ./kickstart_generator.py
- Run 'sudo ./kickstart_generator.py


