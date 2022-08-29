[![GitHub license](https://img.shields.io/github/license/brianlturney/Rocky-Linux-Kickstart-Image-Generator)](https://github.com/brianlturney/Kickstart-ISO-Generator/blob/main/LICENSE)   ![](https://komarev.com/ghpvc/?username=brianlturney)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54&style=flat)

# Kickstart ISO Generator

# Description

This kickstart ISO generator is a fully automated elegant way to create custom ISOs automatically and securely to allow you to auto-install your favorite Fedora linux (RHEL, CentOS, Rocky, etc) on hypervisors or bare metal.

# Backstory

I started this project to automate something I already know. Installing the Linux OS. After much research online into the 'Kickstart' feature of Fedora I saw very few implementations, and even fewer (well none really) that worked. And certainly none that were attempted using python. So liking a challenge and taking the road less traveled I started work on making this work. More than that really, I wanted to make it work with every flavor of Fedora I knew such as RHEL, CentOS, Alma, and Rocky Linux. The later of which has become my new favorite. Rocky Linux 9 is the new quick, bold and lean open source replacement for CentOS which RedHat has recently pulled from being open source. Back to 'Kickstart'. Riddled with poor documentation, bugs, and issues, many out there on the internet struggle with the kickstart feature of Fedora. This Git ends all that and not only solves the issues but makes it work smoothly with all your Fedora favorites. Enjoy! :D

Compatible to run on:
- ![Rocky Linux](https://img.shields.io/badge/-Rocky%20Linux-%2310B981?style=for-the-badge&logo=rockylinux&logoColor=white&style=flat) ![CentOS](https://img.shields.io/badge/cent%20os-002260?style=for-the-badge&logo=centos&logoColor=F0F0F0&style=flat) ![Red Hat Enterprise Linux](https://img.shields.io/badge/Red%20Hat-EE0000?style=for-the-badge&logo=redhat&logoColor=white&style=flat) ![Kali](https://img.shields.io/badge/Kali-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white&style=flat) ![Fedora](https://img.shields.io/badge/Fedora-294172?style=for-the-badge&logo=fedora&logoColor=white&style=flat) 
- and many other Fedora distros...

Compatible to customize ISOs for:
- ![Rocky Linux](https://img.shields.io/badge/-Rocky%20Linux-%2310B981?style=for-the-badge&logo=rockylinux&logoColor=white&style=flat) ![CentOS](https://img.shields.io/badge/cent%20os-002260?style=for-the-badge&logo=centos&logoColor=F0F0F0&style=flat) ![Red Hat Enterprise Linux](https://img.shields.io/badge/Red%20Hat-EE0000?style=for-the-badge&logo=redhat&logoColor=white&style=flat) ![Fedora](https://img.shields.io/badge/Fedora-294172?style=for-the-badge&logo=fedora&logoColor=white&style=flat) 
- and other Fedora distros...

* This has not been engineered yet to run on Debian, Suse, and other non-Fedora distros.

# Requirements

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54&style=flat)

# What it does

1) It will download the ISO you select or add in the kickstart_generator.py
2) Mount the ISO and extract
3) Update the ISO with the advanced Kickstart auto install parameters
4) Check which distribution you are running and choose the best commands to run for success
5) Implant hybridization to the ISO
6) Implant MD5 hash to the ISO
7) Create a BIOS and UEFI hybrid bootable ISO

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

# Troubleshooting

- The ks.cfg here looks for the hdd as sda by default. For nvme0n1 drives uncomment the corresponding lines in the ks.cfg and comment the sda lines.

![alt text](https://github.com/brianlturney/brianlturney/blob/main/kickstart_generator.png?raw=true)

![alt text](https://github.com/brianlturney/brianlturney/blob/main/kickstart_install_start.png?raw=true)

![alt text](https://github.com/brianlturney/brianlturney/blob/main/kickstart_install_start.png?raw=true)

![alt text](https://github.com/brianlturney/brianlturney/blob/main/kickstart_install_finish.png?raw=true)

![alt text](https://github.com/brianlturney/brianlturney/blob/main/Rocky%20Linux%209.png?raw=true)
