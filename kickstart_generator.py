#!/usr/bin/env python
#Linux Kickstart ISO Generator - Brian Turney 08-18-2022

# Import the os module
import os

#Clear the terminal
cmd = "clear"
os.system(cmd)

#Assign color codes
WHITE = '\x1b[1;37;40m'
GREEN = '\x1b[1;32;40m'
BLUE = '\x1b[1;36;40m'
ORANGE = '\x1b[1;33;40m'
RED = '\x1b[1;31;40m'
RED_FLASHING = '\x1b[6;31;40m'

# Set the projects working directories
CWD = "./"
MIRROR_URL = "https://download.rockylinux.org/pub/rocky/9/isos/x86_64/"
SOURCE_ISO_NAME = "Rocky-9.0-x86_64-dvd.iso"
KICKSTART_KS_CFG =  "ks.cfg"
KICKSTART_SPLASH =  "splash.png"
ISO_SOURCE_MOUNT = "mount"
ISO_SOURCE_EXTRACT = "extract"
KICKSTART_ISO_NAME = "Kickstart-"

# Determine OS
with open("/etc/os-release") as distro:
    for line in distro:
        if "centos" in line:
            OS_DISTRO = "CentOS"
            ISOPACKAGE="mkisofs"
            break
        elif "fedora" in line:
            OS_DISTRO = "Fedora"
            ISOPACKAGE="mkisofs"
            break           
        elif "debian" in line:
            OS_DISTRO = "Debian"
            ISOPACKAGE="mkisofs"
            break
        elif "kali" in line:
            OS_DISTRO = "Kali"
            ISOPACKAGE="mkisofs"
            break                                 
        else:
            OS_DISTRO = "This OS is not supported"
print(GREEN + "[ Ok ]" + WHITE + " Current Linux Distro: " + BLUE + OS_DISTRO)       

# Check if the directories exist or not
if not os.path.exists(CWD + ISO_SOURCE_MOUNT):   
    # If not present then create it
    print(ORANGE + "[ Creating ]" + WHITE + " Checking " + ISO_SOURCE_MOUNT + " directory")
    os.makedirs(CWD + ISO_SOURCE_MOUNT)
else:
    print(GREEN + "[ Ok ]" + WHITE + " Checking " + ISO_SOURCE_MOUNT + " directory")
if not os.path.exists(CWD + ISO_SOURCE_EXTRACT):   
    # if not present then create it
    print(ORANGE + "[ Creating ]" + WHITE + " Checking " + ISO_SOURCE_EXTRACT + " directory")
    os.makedirs(CWD + ISO_SOURCE_EXTRACT)
else:
    print(GREEN + "[ Ok ]" + WHITE + " Checking " + ISO_SOURCE_EXTRACT + " directory")

# Check if source ISO already exists
if not os.path.exists(CWD + SOURCE_ISO_NAME):   
    # If not present then create it.
    print(RED + "[ Downloading ] " + WHITE + " Checking source iso file. Not found." + ORANGE)
    cmd = "wget -O " + CWD + SOURCE_ISO_NAME + " " + MIRROR_URL + SOURCE_ISO_NAME + "  -q --show-progress"
    os.system(cmd)
    print(GREEN + "[ Ok ]" + GREEN + " Download Completed" + WHITE)
else:
    print(GREEN + "[ Ok ]" + WHITE + " Source ISO file already exists.")

# Mount ISO image
print(GREEN + "[ Ok ]" + BLUE + " Mounting source ISO" + WHITE)
cmd = "mount " + CWD + SOURCE_ISO_NAME + " " + CWD + ISO_SOURCE_MOUNT
os.system(cmd)

def extract_iso():
    # Extract ISO
    print(GREEN + "[ Ok ]" + BLUE + " Extracting source ISO" + GREEN)
    cmd = "rsync -a --info=progress2 --human-readable " + CWD + ISO_SOURCE_MOUNT + "/ " + CWD + ISO_SOURCE_EXTRACT + "/"
    os.system(cmd)
    print(GREEN + "[ Ok ]" + BLUE + " Extraction Complete" + WHITE)

answer = input("Skip ISO extraction? y or n") 
if answer == "y": 
    print("** Skipping ISO extraction **") 
elif answer == "n":
    extract_iso()
else: 
    print("Please enter yes or no.") 

# Copy kickstart config
print(GREEN + "[ Ok ]" + BLUE + "Copying kickstart config to extracted ISO" + WHITE)
cmd = "cp -a " + CWD + KICKSTART_KS_CFG + " " + CWD + ISO_SOURCE_EXTRACT
os.system(cmd)

# Get the label of the ISO required for the isolinux.cfg file and the mkisfs command
import subprocess
ISO_LABEL = str(subprocess.check_output("echo | grep -oP 'LABEL=+\K[^ ]+' " + CWD + ISO_SOURCE_EXTRACT + "/isolinux/isolinux.cfg | head -1", shell=True))
ISO_LABEL = ISO_LABEL[:-3]
ISO_LABEL = ISO_LABEL[2:]
print(GREEN + "[ Ok ]" + BLUE + " The current ISO label is " + ISO_LABEL + WHITE)

# Boot menu changes
print(GREEN + "[ Ok ]" + BLUE + " Modifying boot parameters" + WHITE)
# For bios boot
cmd = "sed -i 's@append initrd=initrd.img inst.stage2=hd:LABEL=" + ISO_LABEL + " quiet@append initrd=initrd.img inst.text inst.ks=cdrom:/ks.cfg inst.stage2=hd:LABEL=" + ISO_LABEL + "@g' " + CWD + ISO_SOURCE_EXTRACT + "/isolinux/isolinux.cfg"
os.system(cmd)
cmd = "sed -i 's@append initrd=initrd.img inst.stage2=hd:LABEL=" + ISO_LABEL + " rd.live.check quiet@append initrd=initrd.img inst.text inst.ks=cdrom:/ks.cfg inst.stage2=hd:LABEL=" + ISO_LABEL + " rd.live.check@g' " + CWD + ISO_SOURCE_EXTRACT + "/isolinux/isolinux.cfg"
os.system(cmd)
# For uefi boot
#cmd = "sed -i 's@set timeout=60@set timeout=0@g' " + CWD + ISO_SOURCE_EXTRACT + "/EFI/BOOT/grub.cfg"
os.system(cmd)
cmd = "sed -i 's@Install@Kickstart Install@g' " + CWD + ISO_SOURCE_EXTRACT + "/EFI/BOOT/grub.cfg"
os.system(cmd)
cmd = "sed -i 's@1@0@g' " + CWD + ISO_SOURCE_EXTRACT + "/EFI/BOOT/grub.cfg"
os.system(cmd)
cmd = "sed -i 's@install@Kickstart Install Rocky Linux 9.0@g' " + CWD + ISO_SOURCE_EXTRACT + "/EFI/BOOT/grub.cfg"
os.system(cmd)
cmd = "sed -i 's@inst.stage2=hd:LABEL=" + ISO_LABEL + " quiet@inst.ks=cdrom:/ks.cfg inst.stage2=hd:LABEL=" + ISO_LABEL + "@g' " + CWD + ISO_SOURCE_EXTRACT + "/EFI/BOOT/grub.cfg"
os.system(cmd)
cmd = "sed -i 's@inst.stage2=hd:LABEL=" + ISO_LABEL + " rd.live.check quiet@inst.ks=cdrom:/ks.cfg inst.stage2=hd:LABEL=" + ISO_LABEL + " rd.live.check@g' " + CWD + ISO_SOURCE_EXTRACT + "/EFI/BOOT/grub.cfg"
os.system(cmd)
#cmd = "sed -i 's@insmod ext2@insmod ext2 \rinsmod gfxterm \rterminal_output gfxterm \rinsmod gfxterm_background \rinsmod png \rloadfont /EFI/BOOT/fonts/unicode.pf2 \rbackground_image -m stretch /EFI/BOOT/splash.png@g' " + CWD + ISO_SOURCE_EXTRACT + "/EFI/BOOT/grub.cfg"
#os.system(cmd)
#cmd = "sed -i 's@/EFI/BOOT/grub.cfg@/EFI/BOOT/grub.cfg \r/EFI/BOOT/splash.png@g' " + CWD + ISO_SOURCE_EXTRACT + "/images/boot.iso.manifest"
#os.system(cmd)

# Check if kickstart ISO already exists
if not os.path.exists(CWD + KICKSTART_ISO_NAME + SOURCE_ISO_NAME + ".iso"):
    NOTHING = "do"
else:
    cmd = "rm -f " + CWD + KICKSTART_ISO_NAME + SOURCE_ISO_NAME + ".iso"
    os.system(cmd)

# Make kickstart ISO
if OS_DISTRO == "Fedora":
    import importlib.util 
    is_present = importlib.util.find_spec(ISOPACKAGE) #find_spec will look for the package
    if is_present is None:
        print(GREEN + "[ Ok ]" + BLUE + " Checking for ISO package handler" + WHITE)
        cmd = "yum install " + ISOPACKAGE + " -y"
        os.system(cmd)
        print(GREEN + "[ Ok ]" + BLUE + " Creating Kickstart ISO" + WHITE)
        #cmd = "mkisofs -o " + CWD + KICKSTART_ISO_NAME + SOURCE_ISO_NAME + " -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -V '" + ISO_LABEL + "' -boot-load-size 4 -boot-info-table -R -J -v " + CWD + ISO_SOURCE_EXTRACT
        cmd = "mkisofs -relaxed-filenames -J -R -o " + CWD + KICKSTART_ISO_NAME + SOURCE_ISO_NAME + " -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -V '" + ISO_LABEL + "' -boot-load-size 4 -boot-info-table -eltorito-alt-boot -eltorito-platform efi -b images/efiboot.img -no-emul-boot " + CWD + ISO_SOURCE_EXTRACT
        os.system(cmd)
    else:
        print(GREEN + "[ Ok ]" + BLUE + " Creating Kickstart ISO" + WHITE)
        cmd = "mkisofs -relaxed-filenames -J -R -o " + CWD + KICKSTART_ISO_NAME + SOURCE_ISO_NAME + " -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -V '" + ISO_LABEL + "' -boot-load-size 4 -boot-info-table -eltorito-alt-boot -eltorito-platform efi -b images/efiboot.img -no-emul-boot " + CWD + ISO_SOURCE_EXTRACT
        os.system(cmd)

if OS_DISTRO == "Kali":
    import importlib.util 
    is_present = importlib.util.find_spec(ISOPACKAGE) #find_spec will look for the package
    if is_present is None:
        print(GREEN + "[ Ok ]" + BLUE + " Checking for ISO package handler" + WHITE)
        cmd = "apt install " + ISOPACKAGE + " -y"
        os.system(cmd)
        print(GREEN + "[ Ok ]" + BLUE + " Creating Kickstart ISO" + WHITE)
        #cmd = "mkisofs -o " + CWD + KICKSTART_ISO_NAME + SOURCE_ISO_NAME + " -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -V '" + ISO_LABEL + "' -boot-load-size 4 -boot-info-table -R -J -v " + CWD + ISO_SOURCE_EXTRACT
        cmd = "mkisofs -relaxed-filenames -J -R -o " + CWD + KICKSTART_ISO_NAME + SOURCE_ISO_NAME + " -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -V '" + ISO_LABEL + "' -boot-load-size 4 -boot-info-table -eltorito-alt-boot -eltorito-platform efi -b images/efiboot.img -no-emul-boot " + CWD + ISO_SOURCE_EXTRACT
        os.system(cmd)
    else:
        print(GREEN + "[ Ok ]" + BLUE + " Creating Kickstart ISO" + WHITE)
        cmd = "mkisofs -relaxed-filenames -J -R -o " + CWD + KICKSTART_ISO_NAME + SOURCE_ISO_NAME + " -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -V '" + ISO_LABEL + "' -boot-load-size 4 -boot-info-table -eltorito-alt-boot -eltorito-platform efi -b images/efiboot.img -no-emul-boot " + CWD + ISO_SOURCE_EXTRACT
        os.system(cmd)

# Unmount ISO
print(GREEN + "[ Ok ]" + BLUE + " Un-mounting source ISO" + WHITE)
cmd = "umount " + CWD + ISO_SOURCE_MOUNT
os.system(cmd)

# Making hybrid ISO
cmd = "sudo isohybrid --uefi " + CWD + KICKSTART_ISO_NAME + SOURCE_ISO_NAME
print(GREEN + "[ Ok ]" + BLUE + " Hybridizing ISO" + WHITE)

# Injecting MD5 hash
cmd = "sudo implantisomd5 " + CWD + KICKSTART_ISO_NAME + SOURCE_ISO_NAME
print(GREEN + "[ Ok ]" + BLUE + " Embedding MD5 checksum" + WHITE)


print("")
print(GREEN + "[ Ok ]" + BLUE + " Kickstart ISO complete. The ISO file is located in the current working directory" + WHITE)
print("")
print("** PROCESS COMPLETE **")

# The end
