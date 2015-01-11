#!bin/bash
result=${PWD}

echo "Everything will be done in this directory."
echo $result

echo "Enter the name of operating system eg if it is Ubuntu/Debian distro 64bit then type debian64 else for 32 bit debian type debian32 and for rpm distro type rpm64 for 64 bit else rpm32 for 32 bit"
read SYSTEM
sudo mkdir -p /usr/java
#Installation of java according to the type of os 

if [ "$SYSTEM" == debian64 ]; then
    wget http://javadl.sun.com/webapps/download/AutoDL?BundleId=97360
    mv AutoDL?BundleId=97360 jre-8u25-linux-x64.tar.gz
    sudo cp jre-8u25-linux-x64.tar.gz /usr/java/jre-8u25-linux-x64.tar.gz 
    cd /usr/java
    sudo tar zxvf jre-8u25-linux-x64.tar.gz
    sudo rm jre-8u25-linux-x64.tar.gz
    cd $result
elif [ "$SYSTEM" == debian32 ]; then
    wget http://javadl.sun.com/webapps/download/AutoDL?BundleId=97358 
    mv AutoDL?BundleId=97358 jre-8u25-linux-i586.tar.gz
    sudo cp jre-8u25-linux-i586.tar.gz /usr/java/jre-8u25-linux-i586.tar.gz 
    cd /usr/java
    sudo tar zxvf jre-8u25-linux-i586.tar.gz
    sudo rm jre-8u25-linux-i586.tar.gz
    cd $result
elif [ "$SYSTEM" == rpm64 ]; then
    wget http://javadl.sun.com/webapps/download/AutoDL?BundleId=97359
    mv AutoDL?BundleId=97359 jre-8u25-linux-x64.rpm
    sudo cp jre-8u25-linux-x64.rpm /usr/java/jre-8u25-linux-x64.rpm 
    cd /usr/java
    sudo rpm -ivh jre-8u25-linux-x64.rpm
    sudo rm jre-8u25-linux-x64.rpm
    cd $result
elif [ "$SYSTEM" == rpm32 ]; then
    wget http://javadl.sun.com/webapps/download/AutoDL?BundleId=97357 
    mv AutoDL?BundleId=97357 jre-8u25-linux-i586.rpm
    sudo cp jre-8u25-linux-i586.rpm /usr/java/jre-8u25-linux-i586.rpm
    cd /usr/java
    sudo rpm -ivh jre-8u25-linux-i586.rpm
    sudo rm  jre-8u25-linux-i586.rpm
    cd $result
fi

# So the installation of java is complete
cd $result
wget http://www.mpi.nl/tools/elan/ELAN_4-8-1_linux.bin
echo "Install ELAN in current directory in a new folder called ELAN"
chmod +x ELAN_4-8-1_linux.bin
bash ELAN_4-8-1_linux.bin
 
