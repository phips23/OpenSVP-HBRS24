import telnetlib
import time
import re

def query_and_extract_value(tn, command):
    """Sendet einen SCPI-Befehl und extrahiert die letzte Zahl aus der Antwort."""
    time.sleep(1)  # Kurz warten, damit das Gerät die Befehle verarbeiten kann
    tn.write(command.encode("ascii"))  # Befehl senden
    time.sleep(1)  # Kurze Wartezeit, damit die Antwort vollständig kommt
    response = tn.read_until(b"x", timeout=1).decode("ascii")  # Antwort lesen und dekodieren
    print(response)
    
    # Zahlen in der Antwort extrahieren
    numbers = re.findall(r'[+-]?\d*\.\d+|\d+', response)  # Alle Zahlen (auch Dezimalzahlen) finden
    if numbers:
        return numbers[-1]  # Letzte Zahl zurückgeben
    else:
        return None  # Falls keine Zahl gefunden wird

def set_and_get_voltage_and_current(host, port, voltage, max_current, min_current):
    try:
        print(f"Verbinde mit {host}:{port}...")
        tn = telnetlib.Telnet(host, port)
        print("Verbindung erfolgreich hergestellt.")

        # Spannung setzen
        set_voltage_command = f"VOLT {voltage}\n"
        print(f"Sende Befehl: {set_voltage_command.strip()}")
        tn.write(set_voltage_command.encode("ascii"))

        # 1 Sekunde warten, bevor der Strom gesetzt wird
        time.sleep(1)

        # Maximalen Strom setzen
        set_max_current_command = f"CURR:MAX {max_current}\n"
        print(f"Sende Befehl: {set_max_current_command.strip()}")
        tn.write(set_max_current_command.encode("ascii"))

        # Kurz warten, damit das Gerät die Befehle verarbeiten kann
        time.sleep(1)

        # Minimalen Strom setzen
        set_min_current_command = f"CURR:MIN {min_current}\n"
        print(f"Sende Befehl: {set_min_current_command.strip()}")
        tn.write(set_min_current_command.encode("ascii"))

        # Kurz warten, damit das Gerät die Befehle verarbeiten kann
        time.sleep(1)

        # Spannung abfragen und extrahieren
        voltage_value = query_and_extract_value(tn, "VOLT?\n")
        if voltage_value:
            print(f"Eingestellte Spannung: {voltage_value} V")
        else:
            print("Keine gültige Spannung gefunden.")
        
        # Maximalen Strom abfragen und extrahieren
        max_current_value = query_and_extract_value(tn, "CURR:LIM:POS?\n")
        if max_current_value:
            print(f"Eingestellter maximaler Strom: {max_current_value} A")
        else:
            print("Kein gültiger maximaler Strom gefunden.")

        # Minimalen Strom abfragen und extrahieren
        min_current_value = query_and_extract_value(tn, "CURR:LIM:NEG?\n")
        if min_current_value:
            print(f"Eingestellter minimaler Strom: {min_current_value} A")
        else:
            print("Kein gültiger minimaler Strom gefunden.")

        # Verbindung schließen
        tn.close()
        print("Verbindung geschlossen.")

    except Exception as e:
        print(f"Fehler: {e}")

# Verbindungskonfiguration
host = "192.168.10.105"  # IP-Adresse des Geräts
port = 23                # Telnet-Port
voltage = 15             # Spannung in Volt
max_current = 9          # Maximaler Strom in Ampere
min_current = -8         # Minimaler Strom in Ampere

# Funktion ausführen
set_and_get_voltage_and_current(host, port, voltage, max_current, min_current)
