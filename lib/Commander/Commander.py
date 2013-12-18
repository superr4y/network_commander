#!/usr/bin/env python3

class Commander:
    def __init__(self):
        pass

    def configure(self):
        """
        This will setup the home directory and create all config files

        >>> Commander().configure()
        'w00t'
        """
        return 'w00t'

    def run(self):
        pass



if __name__ == '__main__':
    import doctest
    doctest.testmod()

