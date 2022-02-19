import sacn
import time
import pyudmx

dev = pyudmx.uDMXDevice()
dev.open()

receiver = sacn.sACNreceiver()
receiver.start()  # start the receiving thread

class lamp():

    def __init__(self, lamptype):
        self.lamptype = lamptype
        self.dmx_packet = []

    def rgb_to_dmx(self, r, g, b):
        self.dmx_packet[r, g, b]

        if self.lamptype == 'showtec':
            self.dmx_packet += [0, 0, 0]
        elif self.lamptype == 'ledrain':
            self.dmx_packet += [0, 0, 0, 255]

        return self.dmx_packet.
        

lamp_array = [
    lamp('showtec'),    # 0
    lamp('showtec'),    # 7
    lamp('ledrain')     # 13
]


# define a callback function
@receiver.listen_on('universe', universe=1)  # listens on universe 1
def callback(packet):  # packet type: sacn.DataPacket
    dmx_packet = []
    light_pos = 0
    data = list(packet.dmxData)

    for pos in range(0, len(data)):
        if light_pos > len(lamp_array):    
            break

        if pos + 1 % 3 == 0:
            r = data[pos]
            g = data[pos + 1]
            b = data[pos + 2]
            lamp = lamp_array[light_pos]
            dmx_packet += lamp.rgb_to_dmx(r, g, b)
            light_pos += 1
          
    print(dmx_packet)
    dev.send_multi_value(1, dmx_packet)
    

