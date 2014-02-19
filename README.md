## Installation (Ubuntu):
apt-git install python3 python3-tkinter pip3 git lighttpd wireshark tor-arm xterm
pip3 install quik
pip3 install stem
git clone https://git.torproject.org/tor.git

## Setup Bridge
brctl addbr br0
ifconfig lxcbr0 10.0.0.1 netmask 255.255.255.0

Edit: _templates/lxc.conf.tmpl_
lxc.network.link = lxcbr0  <= should be the same name as the one you see in ifconfig result

## Configure NLXCM
Example configuration files are in _conf_ folder.

HttpCommander takes a symlink argument. The value path will be the web root of the web server.
Tor Commander like TorOinionRouterCommander can have a _tor\_bin_ argument for an different tor binary.
Default tor binary is the system installation.
All Commander objects should be in _commanders_ list.

Here is a simple example network configuration:
```
dns = LxcCommander(DnsCommander())
httpd = LxcCommander(HttpCommander(symlink='/tmp'))

tor_net = TorNetworkCommander(
    das=[
        LxcCommander(TorDirectoryAuthorityCommander()),
        LxcCommander(TorDirectoryAuthorityCommander())
    ],
    ors=[
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()) 
    ],
    ops=[
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander())
 
    ],
    hs=[
        LxcCommander(TorHiddenServiceCommander(), 
                     HttpCommander(symlink='/tmp'))
        ]
)

global commanders
commanders = [dns, httpd, tor_net]
```
