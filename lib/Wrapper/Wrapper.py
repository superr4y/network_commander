#!/usr/bin/env python3
from functools import wraps



def Debug(func):
    """
    This Decorator prints the name and args/kwargs of func
    befor execute func
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        debug_output = '{0}({1}, {2})'.format(func.__name__, args, kwargs)
        print(debug_output)
        return func(*args, **kwargs)
    return wrapper
        


def ExecuteOrNot(func):
    """
    This Decorator takes the return value of func.
    If execute=True then clall Popen, you can
    pass kwargs to Popen e.g. stdout=subprocess.STDOUT.
    Default Popen(..., shell=True) you can set func(..., shell=False).
    If execute=False then just return the return value of func.
    To run in background set background=True.
    
    func require **kwargs e.g.:
    func(x, a=True, **kwargs)
    func(x, **kwargs)
    func(**kwargs)
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        cmd = func(*args, **kwargs)
        if ('execute' not in kwargs) or ('execute' in kwargs and kwargs['execute']):
            from subprocess import Popen
            if 'shell' not in kwargs:
                kwargs['shell'] = True

            popen_kwargs = {k: kwargs[k] for k in kwargs if k != 'execute'
                            and k != 'background'}

            return Popen(cmd, **popen_kwargs)
        else:
            return cmd
    return wrapper


def main():
    @ExecuteOrNot
    def ls(file_pattern, **kwargs):
        return 'ls -l {0}'.format(file_pattern)

    print(ls('*.py', execute=True))

if __name__ == '__main__':
    main()


            
