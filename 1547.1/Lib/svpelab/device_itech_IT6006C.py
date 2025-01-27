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
import telnetlib
import time

class IT6006C(object)
    
    def __init__(self, ip="127.0.0.1", port=23):
        self.ip = ip
        self.port = port
        self.timeout = 0.5

    def cmd(self, cmd):
        self.connect()
        command = cmd + "\n"
        self.tn.write(command.encode("ascii"))
        time.sleep(self.timeout)
        self.disconnect()

    def request(self, cmd):
        self.connect()
        command = cmd + "\n"

    def connect(self):
        self.tn = telnetlib.Telnet(self.ip, self.port)
        time.sleep(self.timeout)

    def disconnect(self):
        self.tn.close()