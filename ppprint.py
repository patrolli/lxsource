from inspect import currentframe, getframeinfo


class PPPrint:
    '''
    PPPrint can enhance the 'print' when you use it to debug
    This will print the file path and line number where you insert the 'print'
    '''
    def __init__(self):
        pass
    def __call__(self, *args, **kargs):
        frame = currentframe().f_back
        frameinfo = getframeinfo(frame)
        print(frameinfo.filename, str(frameinfo.lineno)+":", *args, **kargs)

ppprint = PPPrint()


if __name__ == '__main__':
    debug_print = ppprint
    a = 2
    debug_print('hello', a)

