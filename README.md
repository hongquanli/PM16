# PM16
for Thorlabs PM16 power meter
## Installations
### Mac OS
```
brew install libusb
pip3 install pyusb pyvisa pyvisa-py
python3
>>> import pyvisa as visa
>>> rm = visa.ResourceManager()
>>> rm.list_resources()
```
### Ubuntu
```
sudo apt-get install python3-pyusb python3-pyvisa
pip3 install pyusb pyvisa pyvisa-py zeroconf psutil
sudo mv 99-pm16.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
sudo udevadm trigger
python3
>>> import PM16
>>> pm = PM16.PM16()
>>> pm.read()
```
