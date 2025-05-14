from stem import Signal
from stem.control import Controller
import requests, time

TOR_PASSWORD = 'mypassword'

def new_tor_ip():
   with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=TOR_PASSWORD)
        controller.signal(Signal.NEWNYM)
        print("[✔] Meminta pergaintian IP baru...")
        
def ambil_ip():
    sessions = requests.Session()
    sessions.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    ip = sessions.get("http://httpbin.org/ip", timeout=10).json()["origin"]
    return ip

if __name__ == "__main__":
    ip_lama = ambil_ip()
    print(f"IP Lama : {ip_lama}")
    new_tor_ip()
    time.sleep(5) # biyar ada jeda biar ip gak error
    ip_baru = ambil_ip()
    print(f"IP Baru : {ip_baru}")
    if ip_lama != ip_baru:
        print("[✔] IP berhasil diganti.")
    else:
        print("[✘] Gagal mengganti IP.")
    print("[✔] Selesai.")
    