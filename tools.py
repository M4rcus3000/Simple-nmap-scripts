import subprocess
import os
import sys

USER = os.getlogin()
DIR = "/home/%s/Desktop/WorkSpace"%USER

def installAll():
    subprocess.call(["sudo","apt", "update", "-y"])
    subprocess.call(["sudo","apt", "install", "-y", "docker.io"])
    subprocess.call(["sudo","apt", "install", "-y", "can-utils"])
    subprocess.call(["sudo","apt", "install", "-y", "libsdl2-dev", "libsdl2-image-dev"])
    subprocess.call(["sudo", "systemctl", "enable", "docker", "--now" ])
    subprocess.call(["sudo","modprobe", "vcan"])
    subprocess.call(["sudo","ip", "link", "add", "dev", "vcan0", "type", "vcan"])
    subprocess.call(["sudo","ip", "link", "set", "up", "vcan0"])
    subprocess.call(["clear"])

    subprocess.call(["mkdir", "%s/CANalyzator"%DIR])
    subprocess.call(["git","clone", "https://github.com/schutzwerk/CANalyzat0r.git", "%s/CANalyzator"%DIR])
    subprocess.call(["sudo", "make", "build", "-C", "%s/CANalyzator/docker"%DIR])
    subprocess.call(["clear"])
    
    subprocess.call(["mkdir", "%s/ICSim"%DIR])
    subprocess.call(["git","clone", "https://github.com/zombieCraig/ICSim.git", "%s/ICSim"%DIR])
    subprocess.call(["sudo", "make", "all", "-C", "%s/ICSim"%DIR])
    subprocess.call(["clear"])
    
    
if __name__ == '__main__':

    if(os.path.isdir(DIR)):
        subprocess.call(["rm","-rf", DIR])
        subprocess.call(["mkdir", DIR])
    else:
        subprocess.call(["mkdir", DIR])

    subprocess.call(["clear"])
    
    installAll()
    
