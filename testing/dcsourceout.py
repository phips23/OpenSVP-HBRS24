import telnetlib
import time
import re

def query_output_status(host, port):
    """Prüft, ob der Ausgang des Geräts eingeschaltet ist."""
    try:
        print(f"Verbinde mit {host}:{port}...")
        tn = telnetlib.Telnet(host, port)
        print("Verbindung erfolgreich hergestellt.")
        
        # Ausgangsstatus abfragen
        tn.write("OUTP?\n".encode("ascii"))  # SCPI-Befehl senden
        time.sleep(1)  # Kurze Verzögerung, um Antwort zu erhalten
        response = tn.read_until(b"x", timeout=1).decode("ascii")  # Antwort lesen und dekodieren
        
        # Antwort auf Zahlen überprüfen (1 = an, 0 = aus)
        match = re.search(r'\b(0|1)\b', response)
        if match:
            status = int(match.group(1))
            if status == 1:
                print("Der Ausgang ist eingeschaltet.")
            elif status == 0:
                print("Der Ausgang ist ausgeschaltet.")
        else:
            print("Keine gültige Antwort für den Ausgangsstatus erhalten.")
        
        # Verbindung schließen
        tn.close()
        print("Verbindung geschlossen.")
    
    except Exception as e:
        print(f"Fehler: {e}")

# Verbindungskonfiguration
host = "192.168.10.105"  # IP-Adresse des Geräts
port = 23                # Telnet-Port

# Funktion ausführen
query_output_status(host, port)
