# Firewall rules for Windows 7, example V-Ray DR slave server

import os

print 'Deleting firwewall rule'
firewallCmdDelete = 'netsh advfirewall firewall delete rule name=\"V-Ray DR ' + buildName + '\" program=\"' + (volPipeline+vrayBaseLocation+buildName).replace('/','\\') +  '\\maya_vray\\bin\\vray.exe\"'
os.system( firewallCmdDelete )

# Allow the app in the firewall..
print 'Registering firewall rule'
firewallCmdAdd = 'netsh advfirewall firewall add rule name=\"V-Ray DR ' + buildName + '\" dir=in action=allow program=\"' + (volPipeline+vrayBaseLocation+buildName).replace('/','\\') +  '\\maya_vray\\bin\\vray.exe\" enable=yes'
os.system( firewallCmdAdd )
