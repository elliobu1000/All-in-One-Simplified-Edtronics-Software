import smbus

SLAVE_ADDRESS = 0x04    




# class ArduinoConnection(smbus.SMBus):
#     def __init__(self, bus=None, force= False, slave_addr = SLAVE_ADDRESS) -> None:
#         super().__init__(bus, force)
#         self.slave_addr = slave_addr
#         self.data = 0
#     def read(self):
#         self.data = self.read_byte(self.slave_addr)
#         return self.data

#     def write(self,data):
#         self.data = data
#         self.write_byte(self.slave_addr, self.data)
        


ArduinoConn = smbus.SMBus(1)
