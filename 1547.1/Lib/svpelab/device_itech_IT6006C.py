"""
Copyright (c) 2024, Hochschule Bonn-Rhein-Sieg
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.

Neither the names of the Hochschule-Bonn-Rhein-Sieg nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Questions can be directed to philipp.schmitz@h-brs.de or marco.jung@h-brs.de
"""
import pyvisa

class IT6006C(object):
    
    def __init__(self, ip):
        resource = "TCPIP0::"+ip+"::INSTR"
        rm = pyvisa.ResourceManager()
        self.inst = rm.open_resource(resource)
        self.inst.write_termination = '\n'
        self.inst.read_termination = '\n'
        self.inst.timeout = 5000

    def send_command(self, command):
        self.inst.write(command)
        #print(f"Gesendet: {command}")

    def query_device(self, command):
        response = self.inst.query(command)
        #print(f"Antwort: {response.strip()}")
        return response.strip()
    
    def setVoltage(self, v):
        self.send_command("VOLT "+str(v))

    def setPosCurrent(self, i):
        self.send_command("CURR:LIM:POS "+str(i))

    def setNegCurrent(self, i):
        self.send_command("CURR:LIM:NEG "+str(i))

    def getVoltage(self):
        return float(self.query_device("VOLT?"))

    def getMeasVoltage(self):
        return float(self.query_device("MEAS:VOLT?"))

    def getPosCurrent(self):
        return float(self.query_device("CURR:LIM:POS?"))

    def getNegCurrent(self):
        return float(self.query_device("CURR:LIM:NEG?"))

    def getMeasCurrent(self):
        return float(self.query_device("MEAS:CURR?"))

    def outputOn(self):
        self.send_command("OUTP ON")

    def outputOff(self):
        self.send_command("OUTP OFF") 

def main():
    try:
        dc1 = IT6006C(ip='192.168.10.105')
        dc2 = IT6006C(ip='192.168.10.106')
        dc3 = IT6006C(ip='192.168.10.107')
        dc1.outputOff()
        dc2.outputOff()
        dc3.outputOff()
        '''print("test")
        dc.setVoltage(500)
        #print(dc.getVoltage)
        print(dc.getVoltage())
        dc.setNegCurrent(-10)
        print("Vorgabe minimaler Strom:"+dc.getNegCurrent())
        dc.setPosCurrent(10)
        print("Vorgabe maximaler Strom:"+dc.getPosCurrent())
        print("Aktuelle Spannung:"+dc.getMeasVoltage())
        print("Aktueller Strom:"+dc.getMeasCurrent())
        dc.outputOff()'''

    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()