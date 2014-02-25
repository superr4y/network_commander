#!/usr/bin/env python3
from stem.control import Controller
import sys

with Controller.from_port(port=9051) as controller:
    controller.authenticate()
    controller.set_conf(sys.argv[1], sys.argv[2])

