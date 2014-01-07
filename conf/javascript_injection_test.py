dns = LxcCommander(DnsCommander())

httpd = []
httpd.append(LxcCommander(HttpCommander(symlink='/home/user/bin/nlxcm/tools/www/openbsd.org')))
httpd.append(LxcCommander(HttpCommander(symlink='/home/user/bin/nlxcm/tools/www/wikileaks.org')))
httpd.append(LxcCommander(HttpCommander(symlink='/home/user/bin/nlxcm/tools/www/www.secdev.org')))
httpd.append(LxcCommander(HttpCommander(symlink='/home/user/bin/nlxcm/tools/www/matplotlib.org')))
httpd.append(LxcCommander(HttpCommander(symlink='/home/user/bin/nlxcm/tools/www/jsi_attacker')))


tor_net = TorNetworkCommander(
    das=[
        LxcCommander(TorDirectoryAuthorityCommander()),
        LxcCommander(TorDirectoryAuthorityCommander())
    ],
    ors=[
        LxcCommander(TorOnionRouterCommander()), 
        LxcCommander(TorOnionRouterCommander()), 
        LxcCommander(TorOnionRouterCommander()), 
        LxcCommander(TorOnionRouterCommander()), 
        LxcCommander(TorOnionRouterCommander(tor_bin='/home/user/bin/tor/src/or/tor',
                                             nick_name='Mallory'))
    ],
    ops=[
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander(nick_name='Alice'))
    ]
   )

global commanders
commanders = [dns]
commanders += httpd
commanders += [tor_net]
