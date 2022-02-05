class BluetoothDecoder:
    def __init__(self):
        self.value = 120
        self.units = "Voltage"

    def getValue(self):
        return self.value

    def getUnits(self):
        possible = ["Voltage", "Current", "Resistance", "Light", "Temperature"]
        unitNumber = 0 #dummy value
        if unitNumber < possible.len() and possible[unitNumber] != "Invalid" {
            self.units = possible[unitNumber]
        return self.units
