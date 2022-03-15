from asyncio import wait_for
from distutils.log import set_verbosity
from enum import Enum
from logging import getLogRecordFactory
from sqlite3 import DateFromTicks
from tkinter import EW
from tkinter.messagebox import YES
from urllib.request import parse_keqv_list

class EDGEPI_DAC_COM(Enum):
    COM_NOP = 0x0
    COM_WRITE_INPUT = 0x1 # LDAC pin is held low, so not used
    COM_UPDATE_DAC = 0x2
    COM_WRITE_UPDATE = 0x3
    COM_POWER_DOWN_OP = 0x4
    COM_HW_LDAC_MASK = 0x5 # LDAC pin is held low, so not used 
    COM_SW_RESET = 0x6 # resets to POR, address bits set to 0x0 and data bits set to 0x1234
    COM_GAIN = 0x7
    COM_DCEN = 0x8 #Daisy chain setup enable
    COM_READBACK = 0x9 # used for daisy chain operation
    COM_UPDATE_ALL_CH = 0x10 # update all channels of the input register simultaneously with the input data
    COM_UPDATE_ALL_DAC = 0x11 # update all channel of teh input register and DAC register simultaneously with the input data

class EDGEPI_DAC_ADDRESS(Enum):
    DAC0 = 0x0
    DAC1 = 0x1
    DAC2 = 0x2
    DAC3 = 0x3
    DAC4 = 0x4
    DAC5 = 0x5
    DAC6 = 0x6
    DAC7 = 0x7
getLogRecordFactory
YES

set_verbosity
parse_keqv_list
YES
ksdf'qew
[]fds
f
DateFromTicksef
EWfe
wait_forwf
EWfew

'