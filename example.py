import serial
from posnet import cmd

with serial.Serial('/dev/ttyACM0', 9600, bytesize=8, parity='N', stopbits=1, timeout=1) as ser:
    print(ser.name, ser.is_open)

    ser.flushInput()  # flush input buffer, discarding all its contents
    ser.flushOutput()  # flush output buffer, aborting current output

    # Check status
    # cmd(ser, 'scomm')

    # Check status of totalizators
    # cmd(ser, 'stot')

    # Set header
    # &c = center, &b = bold
    # cmd(ser, 'hdrset', {
    #   'tx': '&c&bName of the company'
    # })

    # Update next service maintenance data
    # cmd(ser, 'maintenance', {
    #     'te': 'Service OK',
    #     'da': '2022-01-17'
    # })

    # Print any info on the display
    # cmd(ser, 'dsptxtline', {
    #     'id': '0',
    #     'no': '1',
    #     'ln': 'Hello World!',
    #     'th': '1'
    # })

    # Read serial ports configuration
    # cmd(ser, 'comcfgget', {
    #     'no': '1',
    # })
    # cmd(ser, 'comcfgget', {
    #     'no': '2',
    # })

    # Beeping sound generation
    # cmd(ser, 'beep')

    # Print receipt
    cmd(ser, 'trinit', {
        'bm': '0'
    })
    cmd(ser, 'trline', {
        'na': 'Product A',
        'pr': '3',
        'vt': '0'
    })
    cmd(ser, 'trline', {
        'na': 'Product B',
        'pr': '4',
        'vt': '0'
    })
    cmd(ser, 'trend', {
        'to': '7'
    })
    cmd(ser, 'trcancel')

    # tax rates set
    # cmd(ser, 'vatset', {
    #     'va': '23',
    #     'vb': '8',
    #     'vc': '5',
    #     'vd': '0',
    #     've': '100',
    #     'vf': '101',
    #     'vg': '101'
    # })

    # read output
    # time.sleep(1)
    # out = ''
    # while ser.inWaiting() > 0:
    #     out += ser.read(1).decode("windows-1250")
    # print("\n<< \n\t" + out.replace('\x02', '').replace('\x03', "\n\t"))
