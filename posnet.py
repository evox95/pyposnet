import logging
import time
import serial
import crc16


def cmd(device: serial.Serial, command: str, params=None):
    """
    Prepare and send command to the printer using serial port

    :param device:
    :param command:
    :param params:
    :return:
    """
    if params is None:
        params = {}
    params_list = [command]
    for (k, v) in params.items():
        # print("\n\t\t" + f'{k}{v}')
        params_list.append(f'{k}{v}')
    cmd_str = "\x09".join(params_list)

    # \x02 = STX, \x03 = ETX, \x09 = tab
    # [STX]cmd[tab]CRC16[ETX]
    crc = "{:04X}".format(crc16.crc16xmodem((cmd_str + '\x09').encode('cp1250')))
    c = (b'\x02%s\x09#%s\x03' % (
        cmd_str.encode('cp1250'),
        crc.encode('cp1250'),
    ))
    logging.debug(">>\t" + c.decode('cp1250'))
    device.write(c)

    time.sleep(0.2)
    out = ''
    while device.inWaiting() > 0:
        out += device.read(1).decode("cp1250")
    logging.debug("<<\t" + out.replace('\x02', '').replace('\x03', "\n\t"))
