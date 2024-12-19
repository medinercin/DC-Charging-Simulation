import pyvisa

# PyVISA kaynak yöneticisi
rm = pyvisa.ResourceManager()

# Cihazların yapılandırmaları
devices = {
    "Keithley_2306": {"address": "GPIB0::10::INSTR", "name": "Keithley 2306"},
    "Ametek_SGX": {"address": "GPIB0::11::INSTR", "name": "Ametek Sorensen SGX"},
    "Prodigit_3270": {"address": "GPIB0::12::INSTR", "name": "Prodigit 3270"},
}

# Cihazlarla bağlantı kurulumu
connections = {}
for key, device in devices.items():
    try:
        connections[key] = rm.open_resource(device["address"])
        print(f"{device['name']} cihazına başarıyla bağlanıldı.")
    except Exception as e:
        print(f"{device['name']} cihazına bağlanılamadı: {e}")

# Keithley 2306: Batarya şarjı simülasyonu
def keithley_battery_simulation():
    if "Keithley_2306" in connections:
        keithley = connections["Keithley_2306"]
        keithley.write("*RST")  # Cihazı sıfırla
        keithley.write("SOUR:CURR 1.5")  # Akımı 1.5A olarak ayarla
        keithley.write("SOUR:VOLT 3.6")  # Gerilimi 3.6V olarak ayarla
        keithley.write("OUTP ON")        # Çıkışı aç
        print("Keithley 2306: Batarya şarj simülasyonu başlatıldı.")
    else:
        print("Keithley 2306 cihazına bağlantı yok.")

# Ametek SGX: Sabit voltaj/akım ile güç kaynağını ayarla
def ametek_power_supply():
    if "Ametek_SGX" in connections:
        ametek = connections["Ametek_SGX"]
        ametek.write("*RST")  # Cihazı sıfırla
        ametek.write("VOLT 360")  # Gerilimi 360V olarak ayarla
        ametek.write("CURR 50")  # Akımı 50A olarak ayarla
        ametek.write("OUTP ON")  # Çıkışı aç
        print("Ametek SGX: Güç kaynağı aktifleştirildi.")
    else:
        print("Ametek SGX cihazına bağlantı yok.")

# Prodigit 3270: Elektronik yük simülasyonunu ayarla
def prodigit_load_simulation():
    if "Prodigit_3270" in connections:
        prodigit = connections["Prodigit_3270"]
        prodigit.write("*RST")  # Cihazı sıfırla
        prodigit.write("LOAD:MODE CC")  # Yük modunu sabit akım olarak ayarla
        prodigit.write("LOAD:CURR 27.8")  # Akımı 27.8A olarak ayarla
        prodigit.write("LOAD:VOLT 360")  # Gerilimi 360V olarak ayarla
        prodigit.write("LOAD ON")        # Yükü aktifleştir
        print("Prodigit 3270: Yük simülasyonu başlatıldı.")
    else:
        print("Prodigit 3270 cihazına bağlantı yok.")

# Simülasyonları başlat
keithley_battery_simulation()
ametek_power_supply()
prodigit_load_simulation()

# Bağlantıları kapat
for key, conn in connections.items():
    conn.close()
    print(f"{key} cihazı ile bağlantı kapatıldı.")
