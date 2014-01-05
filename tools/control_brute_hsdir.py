from stem.control import Controller

with Controller.from_port(port=9051) as controller:
    controller.authenticate()
    resp = controller.msg('BRUTEHSDIR c22v2bqmiscz4kyv 10 0')
    
    print(resp)