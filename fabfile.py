from __future__ import with_statement
from fabric.api import *

from fabric.contrib.console import confirm
from fabric.contrib.files import exists
from datetime import datetime
import sys, pprint, time, ConfigParser, os

def vagrant():

    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['192.168.100.15']
 
    # use vagrant ssh key
    result = local('vagrant ssh-config xnatview | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]
    

def vmware():

    # set this to your vmware settings
    # if you've used a desktop distro, install an ssh server 
    #
    #   sudo apt-get install openssh-server
    # 
    
    env.user = 'stonerri'
    env.hosts = ['172.16.141.133']


def sysinfo():
    run('uname -a')
    run('lsb_release -a')


def base():

    '''[create] Basic packages for building, version control'''
    with settings(warn_only=True):

        run("sudo apt-get -y update", pty = True)
        run("sudo apt-get -y upgrade", pty = True)

        packages = [
            'php5',
            'apache2',
            'libapache2-mod-python',
            'gcc-4.4',
            'g++',
            'libxml2-dev',
            'mercurial',
            'build-essential',
            'subversion',
            'git',
            'unzip',
            'curl',
            'libcurl3',
            'libcurl3-dev',
            'php5-curl',
            'libdcmtk2',
            'python-setuptools',
            'python-pip',
            'python-dev',
            'python-lxml'
        ]

        packagelist = ' '.join(packages)

        run('sudo apt-get -y install %s' % packagelist, pty = True)

def xnatview():

    '''[install] base python dependencies'''

    with settings(warn_only=True):

        packages = [
            'httplib2',
            'pyxnat'
        ]

        for each_package in packages:
             print each_package
             run('sudo pip install %s' % each_package, pty = True)


def configureXV():

    '''[configure] set some default parameters and restart apache'''

    with settings(warn_only=True):

        # link to enable modpython
        sudo('ln -s /vagrant/xnatsite /etc/apache/sites-enabled/100-xnatsite')

        # link to xnatview folder in vagrant directory
        sudo('ln -s /vagrant/web_code /var/www/xnatview_dev')

        # restart apache2 via apache2ctl
        sudo('apache2ctl restart')

        import webbrowser
        webbrowser.open_new_tab('http://192.168.100.15/xnatview_dev/')





