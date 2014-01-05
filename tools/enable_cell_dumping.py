#!/usr/bin/env python3
from stem.control import Controller

with Controller.from_port(port=9051) as controller:
    controller.authenticate()
    controller.set_conf('DumpCells', '1')

