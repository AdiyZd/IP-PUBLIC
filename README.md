# IP-PUBLIC

---
## LANGKAH-LANGKAH INSTALASI:
**1. Tor Installation dan Setup**
<br>
- Install Tor di Debian/Ubuntu:
```bash
sudo apt update && sudo apt install tor -y
```
**2. buat Tor Password Hash**
<br>
- Pengecekan gunakan script berikut:

```bash
tor --hash-password mypassword
```

**3. Config Tor**
<br>
- Edit Tor configuration file:

```bash
sudo nano /etc/tor/torrc
```
- tambahkan file di paling bawah setingan: 
```bash

ControlPort 9051 
HashedControlPassword 16: <PASSWORD HASH KAMU DAN TANPA <> >
```

**4. Verify Tor ControlPort**

```bash
netstat -tulpen | grep 9051
```

**5. Restart Tor**

```bash
sudo systemctl restart tor
```

**6. Python Installation**

```bash
pip install stem requests
```

- **Alternative** using virtual environment (VENV)

```bash
python3 -m venv venv 
source venv/bin/activate
pip install requests[socks]
pip install PySocks
```
**Install Tor :**
```bash
sudo apt update && sudo apt install tor -y
```
**Jalankan Tor:**
```bash
tor
```


**7. Tor Service Management**
<br>
- Check Tor status:
```bash
sudo systemctl status tor
```
- Start tor:
```bash
sudo systemctl start tor
```

**9. start code**
```bash
Run Python Script
```

**10. enjoyy brooo**
<br>
---


### ⚠️ Penjelasan:
- **Penggunaan Heading:** Saya menggunakan heading yang sesuai untuk membagi bagian-bagian yang penting dalam panduan.
- **Langkah demi Langkah:** Setiap langkah yang diperlukan dijelaskan dengan perintah terminal yang relevan, menjadikannya lebih mudah diikuti.
- **Bagian Troubleshooting:** Ini akan membantu pengguna yang mungkin mengalami masalah saat mengonfigurasi atau menjalankan skrip.
