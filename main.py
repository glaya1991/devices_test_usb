#!/usr/bin/env python3

import sys
import string  # , keyboard
from os import terminal_size

import serial.tools.list_ports
import serial
import time
import os
import random

# py-files
import  tests_eg


# ----- Send/receive function: MODBUS --------- #
def send_recv_msg(msg):
    '''
    in1=input(">> data TX: ")

    # linux
    #ser.write(in1.encode()) #linux

    # windows
    in2 = in1.split(' ')
    in3 = []
    for val in in2:
        in3.append(int(val, 16))
    ser.write(in3)
    '''

    query = [ord(i) for i in msg]

    # print sending message
    # in hex
    #print(''.join('{:02X} '.format((val)) for val in query))
    # string
    print(">> ", msg)
    ser.write(query)

    n = ser.in_waiting
    delay_cnt = 0
    while n == 0 and delay_cnt < 100:
        n = ser.in_waiting
        delay_cnt += 1
        time.sleep(tdelay)

    out = []
    delay_cnt = 0
    # print(n)
    while (n != 0) and delay_cnt < 100:
        out.extend(ser.read(n))
        delay_cnt += 1
        time.sleep(tdelay)
        n = ser.in_waiting
        # print(n)

    n = len(out)
    char_pt = ord('.')
    #print('n = ', n)
    if n != 0:
        print("n={:d}: ".format(n), end=' ')

        if mode == 'hex':
            for i in out:
                print("{:x}".format(i), end=' ')

        elif mode == 'dec':
            for i in out:
                print("{:d}".format(i), end=' ')

        elif mode == 'sym':
            for i in out:
                try:
                    if (i==0xa) or (i==0xd): i = char_pt       # doesn't work, if <14
                    print(chr(i), end='')
                except:
                    print('x', end=' ')

            print('\r\n', out, end=' ')

        else:
            print(out, end=' ')

        print("\r\n")
    else:
        print('Wrong request')

    return

def recv_msg():
    n = ser.in_waiting
    delay_cnt = 0
    while n == 0 and delay_cnt < 40:
        n = ser.in_waiting
        delay_cnt += 1
        time.sleep(tdelay)

    out = []
    delay_cnt = 0
    # print(n)
    while (n != 0) and delay_cnt < 40:
        out.extend(ser.read(n))
        delay_cnt += 1
        time.sleep(tdelay)
        n = ser.in_waiting
        # print(n)

    char_pt = ord('.')
    n = len(out)
    if n != 0:
        print("n={:d}: ".format(n), end=' ')

        if mode == 'hex':
            for i in out:
                print("{:x}".format(i), end=' ')

        elif mode == 'dec':
            for i in out:
                print("{:d}".format(i), end=' ')

        elif mode == 'sym':
            for i in out:
                try:
                    if (i == 0xa) or (i == 0xd): i = char_pt  # doesn't work, if <14
                    print(chr(i), end='')
                except:
                    print('x', end=' ')

            print('\r\n', out, end=' ')

        else:
            print(out, end=' ')

        print("\r\n")

    return

# ------------------------------------- #
#        MAIN                           #
# ------------------------------------- #

# linux:
# _port = '/dev/ttyUSB0'

# Win
com_port = 'COM18'
baudrate = 2000000  # 115200
N_TX = 512
mode = 'hex'
dict_mode = {'1': 'hex', '2': 'dec', '3': 'sym'}

tdelay = 0.001
_wr_en = 0

# available com ports
comlist = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(comlist):
    print("{}: {} [{}]".format(port, desc, hwid))

# ----- Set serial port parametrs ----- #

# !!!! UNCOMMENT ME  !!!!
# input1 = input(">> Default settings? - yes=1, no=2, q=quit, h=help\n>>")  # /dev/ttyUSB0
input1 = 1

if (input1 == '2'):
    com_port = input(">> Port: ")
    baudrate = input(">> Baudrate: ")
    try:
        N_TX = int(input(">> N_TX: "))
    except Exception:
        print("Wrong! (default: N_TX=32)")
        N_TX = 32
elif (input1 == 'q'):
    exit()
elif (input1 == 'h'):
    # help_func()
    exit()
else:
    pass

# !!!! UNCOMMENT ME  !!!!
# in1 = input(">> Mode: HEX=1, DEC=2, SYMBOL=3, q=quit: ")
in1 = '3'

mode = dict_mode.get(in1)
if mode == None:
    mode = 'hex'
if in1 == 'q':
    exit()


# ----- Create file (if need!) ---------- #

wr_en = _wr_en
# write rx data:
if wr_en == 1:
    t0 = time.localtime()
    date0 = '{:04d}{:02d}{:02d}'.format(t0.tm_year, t0.tm_mon, t0.tm_mday)
    time0 = '{:02d}:{:02d}:{:02d}'.format(t0.tm_hour, t0.tm_min, t0.tm_sec)
    filename = os.getcwd() + '/rxdata_' + date0 + '_' + time0 + '.txt'
    file1 = open(filename, 'w')
    print(filename, '\r\n')

print('!!! Exit - Ctrl+Shift+C !!!')

# ----- Open serial port -------------- #

try:
    ser = serial.Serial(
        port=com_port,  # '/dev/ttyUSB0', 'COM1'
        baudrate=baudrate,
        # parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
except Exception:
    print('No such port!')
    exit()

if (ser.isOpen() == True):
    print("Port is already opened!")
else:
    try:
        ser.open()
    except Exception:
        print('Cannot open port!')
        exit()
    print("Port is open!")

print(ser.name)
n = ser.in_waiting
out = ser.read(n)  # first read???


# ----- main loop --------------------- #

# ----- TEST EG (ELECTROGARNITURA) ---- #

print("Msg_type: \r\nEG: 0 - components, 1 - device, 2 - wifi_init, 3 - impedance, 4 - thread_eeg, 5 - p300\r\nother - exit, q - exit\r\n")

ch_exit = "n"
while ch_exit == "n":

    msg_type = input("\r\nprint num:  ")
    msg_times = int(input("\r\nprint num of sending:  "))

    if msg_type == '0':
        msg = tests_eg.msg_components
    elif msg_type == '1':
        msg = tests_eg.msg_device
    elif msg_type == '2':
        msg = tests_eg.msg_wifi_init
    elif msg_type == '3':
        msg = tests_eg.msg_impedance
    elif msg_type == '4':
        msg = tests_eg.msg_thread_eeg
    elif msg_type == '5':
        msg = tests_eg.msg_p300
    elif msg_type == 'q':
        print('Exit!')
        exit()
    else:
        exit()

    len_msg = len(msg)
    for t in range(msg_times):
        for i in range(len_msg):
            time.sleep(1)
            send_recv_msg(msg[i])
            for j in range(4):
                recv_msg()

    ch_exit = input("\r\nExit: y/n?  ")


ch_exit = "n"
while ch_exit == "n":
    recv_msg()
    #pass


print('Exit: Ok!')
