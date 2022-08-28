#################################################################
#								#
#		Rocky Linux 9.0 (Blue Onyx)			#
#								#
#		Kickstart Auto-installer File			#
#		created by: Brian Turney			#
#		https://github.com/brianlturney			#
#								#
#################################################################

# System bootloader configuration
# bootloader --append="crashkernel=auto" --location=mbr --boot-drive=nvme0n1 # Uncomment this line for nvme drives.
bootloader --append=" crashkernel=auto" --location=mbr --boot-drive=sda 

# Partition clearing information
#clearpart --all --drives=nvme0n1 --initlabel # Uncomment this line for nvme drives.
clearpart --all --drives=sda

# Partition information (To encrypt the partition add: --encrypted --luks-version=luks2 --passphrase=P@ssword)
autopart --type=lvm

# Manual partitioning: Disk partitioning information for a 1TB drive
#part /boot --fstype="xfs" --ondisk=nvme0n1 --size=1024 --fsoptions="nosuid,nodev"
#part /boot/efi --fstype="efi" --ondisk=nvme0n1 --size=600 --fsoptions="umask=0077,shortname=winnt,nodev"
#part swap --fstype="swap" --ondisk=nvme0n1 --size=15384
#part pv.4675 --fstype="lvmpv" --ondisk=nvme0n1 --size=958753

# Use text install
text

# Install source
#url --url="http://iad.mirror.rackspace.com/rocky/9.0/BaseOS/x86_64/os/" #Musch Slower but still gets the job done.
cdrom #FAST - Choose this option for a faster local install from cdrom or ISO.

# Keyboard layouts
keyboard --vckeymap=us --xlayouts='us'

# System language
lang en_US.UTF-8

# License agreement
eula --agreed

# Network information
network --onboot=yes --bootproto=dhcp --noipv6 --activate --hostname=rockylinux-custom.localdomain

# To create user password hashes use the command: python3 -c 'import crypt,getpass; print(crypt.crypt(getpass.getpass()))'
# The password below for both root and administrator users is P@ssword 
# If you don't care about hashing the passwords (not recommended), simply use the lines below
#Root password=P@ssword

# Create root user
rootpw --iscrypted $6$INireMy4ZLQwW7NN$btkLm/dwn9qV/XWW8dhDd2hjKHk8tj59q.Q8qSW7i4LojhPYWXDx4YRWxXQ/.30E8ND3IcImJ.pys3DyYwco0.

# Create additional users
user --name=administrator --groups=dialout,kvm,libvirt,qemu,wheel --password=$6$f9y8RhpOf4kppQlt$FpXm5aOecAV8Hf9DQM4/gHMD.EPbkacI36OQEyS50Iqs0Y2fLnOWeEPGXDhaVZjHpNF4RhEdyRDxBDByffCGH/ --iscrypted --gecos="Administrator"
#user --groups=dialout,kvm,libvirt,qemu,wheel --name=administrator --password=P@ssword --gecos="administrator"

# Run the Setup Agent on first boot
firstboot --disable

# X Window System configuration information
xconfig  --startxonboot

# System services
services --enabled="chronyd"

# System timezone
timezone America/Chicago --utc		# CST | UTC−06:00

# Example timezone list
#timezone America/Los_Angeles --utc	# PST | UTC−08:00
#timezone America/Denver --utc		# MST | UTC−07:00
#timezone America/Chicago --utc		# CST | UTC−06:00
#timezone America/New_York --utc	# EST | UTC−05:00
#timezone Australia/Sydney --utc	# UTC+10:00
#timezone Australia/Perth --utc		# UTC+08:00
#timezone Europe/Saratov --utc		# UTC+04:00
#timezone Europe/London --utc		# UTC+00:00
#timezone Asia/Hong_Kong --utc		# UTC+08:00
#timezone Asia/Calcutta --utc		# UTC+05:30

%packages
@^workstation-product-environment
createrepo
dnf-automatic
genisoimage
isomd5sum
kexec-tools
libatomic
liberation-fonts
libuv
libvirt
libvirt-client
libvirt-daemon
libXScrnSaver
nss-tools
open-vm-tools
open-vm-tools-desktop
policycoreutils-python-utils
qt5-qtquickcontrols
qt5-qtx11extras
syslinux
virt-install
virt-manager
virt-viewer
vulkan-loader
yum-utils
zstd
%end

# The state of the machine after the install completes. Leave commented for no action.
#shutdown
#reboot

# Post nochroot
%post --interpreter=/usr/bin/bash --nochroot --log=/mnt/sysimage/root/ks-post.log

# Configure SELinux
setsebool -P domain_kernel_load_modules on

# Enable Automatic security updates via dnf-automatic
sed -i s/'upgrade_type = default'/'upgrade_type = security'/ /etc/dnf/automatic.conf
sed -i s/'apply_updates = no'/'apply_updates = yes'/ /etc/dnf/automatic.conf
systemctl enable dnf-automatic.timer

# Bring network interfaces up
#for i in $(nmcli -g NAME con show); do nmcli con up "$i"; done;

# Install EPEL repository and packages
dnf --nogpgcheck -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm

# DCONF update for GDM modifications
dconf update

# Optional: Lock root account
#passwd -l root

# Optional: Set user password age minimum
#chage -M 99999 administrator

# Password and security policies
#%anaconda
#pwpolicy root --minlen=6 --minquality=1 --notstrict --nochanges --notempty
#pwpolicy user --minlen=6 --minquality=1 --notstrict --nochanges --emptyok
#pwpolicy luks --minlen=6 --minquality=1 --notstrict --nochanges --notempty
#%end

%end
#################################################################
