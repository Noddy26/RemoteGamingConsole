#####
# Spec file for GamingServer
#####

%define name GamingServer
%define pwd %(pwd)
%define src /root/Server_code
%define version 1.0
%define release PA1
%define arch noarch
%define dependency bash, python > 3, python-yaml >= 3.10, termcolor, MySQLdb, mysql.connector, picamera, flask, flask-cors

# where the files should be saved
%define prefix /home/pi/GamingServer

# The (base) name of the package, which should match the SPEC file name
Name: %{name}

# The upstream version number of the software.
Version: %{version}

# The initial value should normally be 1%, this value should be incremented each new release of the package and reset to 1 when a new Version of the software is built.
Release: %{release}

# A brief, one-line summary of the package.
Summary: The GamingServer is a package that can let you play your console anywhere

# The license of the software being packaged. For packages that are destined for community distributions such as Fedora this must be an Open Source License abiding by the specific distribution’s Licensing Guidelines.
License: (c) Neil Morrison

# The full URL for more information about the program (most often this is the upstream project website for the software being packaged).
URL: http//:193.168.1.13:2000

# If the package is not architecture dependent, i.e. written entirely in an interpreted programming language, this should be BuildArch: noarch otherwise it will automatically inherit the Architecture of the machine it’s being built on.
BuildArch: %{arch}

# A comma or whitespace separated list of packages required by the software to run once installed. There can be multiple entries of Requires each on its own line in the SPEC file.
Requires: %{dependency}

AutoReqProv: no

%description

#####
# Preparation phase
#####
%prep
#!/bin/sh
if [ ! -z ${RPM_BUILD_DIR} ]; then
    sudo rm -rf ${RPM_BUILD_DIR}/*
fi
if [ ! -z ${RPM_BUILD_ROOT} ]; then
    sudo rm -rf ${RPM_BUILD_ROOT}/*
fi
mkdir -p ${RPM_BUILD_ROOT}/%{prefix}
cd %{src}
sudo tar --exclude='*.pyo' --exclude='*.db' --exclude='*.pyc' --exclude='*/.git*' --exclude='*/.idea*' --exclude='Gaming.spec' --exclude='*delete_me*' -cpf - . | tar -C ${RPM_BUILD_ROOT}/%{prefix} -xvf -
cd ${RPM_BUILD_ROOT}
find -L .%{prefix} -depth -print | sed -e 's/^\.//' -e 's/.*/"\0"/' > ${RPM_BUILD_DIR}/GamingServer_files

#####
# Clean-up phase
#####
%clean
if [ ! -z ${RPM_BUILD_DIR} ]; then
    sudo rm -rf ${RPM_BUILD_DIR}/*
fi
if [ ! -z ${RPM_BUILD_ROOT} ]; then
    sudo rm -rf ${RPM_BUILD_ROOT}/*
fi

#####
# Pre-installation phase
#####
%pre

#####
# Post-installation phase
#####
%post
#!/bin/sh
echo -e 'GamingServer tool was installed successfully.\nPlease set up the tool by running the command:\npython3 /home/pi/GamingServer --setup' > /dev/stdout

#####
# Pre-uninstallation phase
#####
%preun

#####
# Post-uninstallation phase
#####
%postun
if [ "$1" == "0" ];then
    sudo rm -rf %{prefix}
    # Prompt message telling the user that the tool has been uninstalled
    echo 'GamingServer tool was uninstalled successfully.' > /dev/stdout
elif [ "$1" == "1" ];then
    echo 'GamingServer tool is being upgraded' > /dev/stdout
    if [ echo $? == "0" ];then
        echo "upgrading"
    fi
fi

#####
# Files included in package
#####
%files -f GamingServer_files
