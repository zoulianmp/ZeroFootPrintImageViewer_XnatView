ZeroFootPrintImageViewer_XnatView
=================================

Vagrant configuration.

### Installation

1. Install virtualbox

2. Install vagrant

3. Clone repository

4. Cd into repository

5. Type command to init vm

    vagrant up

6. Type command to provision (you'll need to manually skip through the GRUB config)

    fab vagrant base

7. Type command to configure xnatview

    fab vagrant xnatview configureXV


8. Visit [http://192.168.100.15/xnatview_dev/](http://192.168.100.15/xnatview_dev/)




