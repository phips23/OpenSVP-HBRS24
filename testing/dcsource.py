import pyvisa

def connect_to_power_supply(resource_name):
    """Verbindet sich mit der IT6006C-500-40 DC-Quelle über Ethernet."""
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource(resource_name)
    inst.write_termination = '\n'  # Standardmäßige Terminierung für SCPI
    inst.read_termination = '\n'
    return inst

def send_command(inst, command):
    """Sendet einen SCPI-Befehl an das Gerät."""
    inst.write(command)
    print(f"Gesendet: {command}")

def query_device(inst, command):
    """Sendet einen SCPI-Befehl und gibt die Antwort zurück."""
    response = inst.query(command)
    print(f"Antwort: {response.strip()}")
    return response.strip()

def main():
    resource = "TCPIP0::192.168.10.105::INSTR"  # Ethernet-Resource-Name
    try:
        inst = connect_to_power_supply(resource)
        
        # Einschalten des Ausgangs
        #send_command(inst, "OUTPut ON")
        
        # Spannung setzen
        send_command(inst, "VOLTage 12.0")  # Setzt 12V
        
        # Strombegrenzung setzen
        #send_command(inst, "CURRent 5.0")  # Setzt 5A
        
        # Abfrage der aktuellen Ausgangsspannung
        voltage = query_device(inst, "VOLTage?")
        
        # Abfrage des aktuellen Ausgangsstroms
        current = query_device(inst, "MEASure:CURRent?")
        
        print(f"Messwerte -> Spannung: {voltage} V, Strom: {current} A")
        
        # Ausschalten des Ausgangs
        send_command(inst, "OUTPut OFF")
        
        inst.close()
    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()
