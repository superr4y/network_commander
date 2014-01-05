dns = LxcCommander(DnsCommander())

httpd = []
httpd.append(LxcCommander(HttpCommander(symlink='/home/user/bin/network_commander/tools/www/openbsd.org')))
httpd.append(LxcCommander(HttpCommander(symlink='/home/user/bin/network_commander/tools/www/wikileaks.org')))
httpd.append(LxcCommander(HttpCommander(symlink='/home/user/bin/network_commander/tools/www/www.secdev.org')))
httpd.append(LxcCommander(HttpCommander(symlink='/home/user/bin/network_commander/tools/www/matplotlib.org')))



nc = LxcCommander(NetCatCommander())
tor_net = TorNetworkCommander(
    das=[
        LxcCommander(TorDirectoryAuthorityCommander()),
        LxcCommander(TorDirectoryAuthorityCommander()),
        LxcCommander(TorDirectoryAuthorityCommander()),
        LxcCommander(TorDirectoryAuthorityCommander())
    ],
    ors=[
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
                LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
                LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
                LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
                LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
                LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander(tor_bin='/home/user/bin/tor/src/or/tor',
                                             nick_name='Mallory')),
        LxcCommander(TorOnionRouterCommander(tor_bin='/home/user/bin/tor/src/or/tor',
                                             nick_name='Mallory'))
    ],
    ops=[
        LxcCommander(TorOnionProxyCommander(nick_name='Alice')), #tor_bin='/home/user/bin/tor/src/or/tor')),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
                LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
                LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander())
    ],
    hs=[
        LxcCommander(TorHiddenServiceCommander(), #tor_bin='/home/user/bin/tor/src/or/tor'), 
                     HttpCommander(symlink='/home/user/bin/network_commander/tools/www/matplotlib.org'))
        ]
)

'''
commander.py only use the commanders list
commanders[0] gets 10.0.0.2 as IP address
commanders[1] gets 10.0.0.3 as IP address
...
'''
global commanders
commanders = [dns]
commanders += httpd
commanders += [tor_net, nc]

#tree = {
#    'lxc_0':{'obj': lxc_commander_obj, 'da_0': da_commander},
#    'lxc_1':{...}
#}
