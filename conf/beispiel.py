dns = LxcCommander(DnsCommander())
httpd = LxcCommander(HttpCommander(symlink='/home/user/bin/nlxcm/tools/www/matplotlib.org'))

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
        LxcCommander(TorOnionProxyCommander())
    ]
    )

global commanders
commanders = [dns, httpd, tor_net]
