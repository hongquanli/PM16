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
