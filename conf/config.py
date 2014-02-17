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
