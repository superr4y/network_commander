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
        LxcCommander(TorOnionRouterCommander(tor_bin='/home/user/bin/tor/src/or/tor',
                                             nick_name='Mallory'))
    ],
    ops=[ LxcCommander(TorOnionProxyCommander(nick_name='Alice')) ]

   )

global commanders
commanders = [dns, httpd, tor_net]
