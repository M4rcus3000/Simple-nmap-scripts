#!/bin/bash
apt update -y
apt install maltego -y
apt install snapd -y
systemctl start snapd
snap install amass
snap install --edge amass
snap refresh
export PATH=$PATH:/snap/bin
mkdir /home/kali/Desktop/test
amass enum -active -d iteso.mx -src -ip -o /home/kali/Desktop/test/iteso.mx.txt
amass enum -active -d ssoiteso.mx -src -ip -o /home/kali/Desktop/test/ssoiteso.mx.txt
