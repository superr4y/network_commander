dns = LxcCommander(DnsCommander())
httpd = LxcCommander(HttpCommander(symlink='/home/user/bin/nlxcm/tools/www/wikileaks.org'))

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
        LxcCommander(TorOnionRouterCommander(
            tor_bin='/home/user/workspace/Tor/src/or/tor', nick_name='mallory')),
        LxcCommander(TorOnionRouterCommander(
            tor_bin='/home/user/workspace/Tor/src/or/tor', nick_name='mallory')),
        LxcCommander(TorOnionRouterCommander(
            tor_bin='/home/user/workspace/Tor/src/or/tor', nick_name='mallory')),
        LxcCommander(TorOnionRouterCommander(
            tor_bin='/home/user/workspace/Tor/src/or/tor', nick_name='mallory')),
        LxcCommander(TorOnionRouterCommander(
            tor_bin='/home/user/workspace/Tor/src/or/tor', nick_name='mallory')),
        LxcCommander(TorOnionRouterCommander(
            tor_bin='/home/user/workspace/Tor/src/or/tor', nick_name='mallory')),
        LxcCommander(TorOnionRouterCommander()) 
    ],
    ops=[
        LxcCommander(TorOnionProxyCommander(nick_name='alice')),
        LxcCommander(TorOnionProxyCommander()) 
    ],
    hs=[
        LxcCommander(TorHiddenServiceCommander(), 
                     HttpCommander(symlink='/home/user/bin/nlxcm/tools/www/openbsd.org')),
        LxcCommander(TorHiddenServiceCommander(), 
                     HttpCommander(symlink='/home/user/bin/nlxcm/tools/www/wikileaks.org'))

        ]
)

global commanders
commanders = [dns, httpd, tor_net]
