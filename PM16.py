import pyvisa as visa

class PM16:
    def __init__(self, address:str) -> None:
        self.rm = visa.ResourceManager()
        self.pm = self.rm.open_resource(address)
        self.wavelength = 500
        self.averaging = 10
        self.set_unit("W")
        self.set_averaging(self.averaging)
        self.set_auto_range(True)
        self.set_wavelength(self.wavelength)
    
    def read(self) -> float:
        return float(self.pm.query("MEAS:POW?"))

    def set_wavelength(self, wavelength:int) -> None:
        self.wavelength = wavelength
        self.pm.write(f"SENS:CORR:WAV {wavelength}")

    def set_averaging(self, averaging:int) -> None:
        self.averaging = averaging
        self.pm.write(f"SENS:AVER {averaging}")

    def set_auto_range(self, auto_range:bool) -> None:
        if auto_range:
            self.pm.write("SENS:RANGE:AUTO ON")
        else:
            self.pm.write("SENS:RANGE:AUTO OFF")

    def set_unit(self, unit:str) -> None:
        self.pm.write(f"SENS:POW:UNIT {unit}")
