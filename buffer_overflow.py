from ctypes import *
msvcrt=cdll.msvcrt
raw_input("once the debugger is attached,press any key to overflow..")
buffer=c_char_p("AAAAA")
overflow="A" * 100
msvcrt.strcpy(buffer,overflow)