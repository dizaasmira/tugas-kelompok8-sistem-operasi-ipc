import socket
import json
import sys

# Ambil parameter dari command line (default: P001 dan qty 1)
product_id = sys.argv[1] if len(sys.argv) > 1 else "P001"
qty = int(sys.argv[2]) if len(sys.argv) > 2 else 1

# Siapkan data payload berformat JSON
payload = {
    "product_id": product_id,
    "qty": qty
}

# Membuat koneksi TCP ke Stock Socket Server (Port 8002)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8002))

print(f"[Order Service Socket] Mengirim request ke Stock Service: {payload}")
client.send(json.dumps(payload).encode('utf-8'))

# Menerima respons dari server
response_data = client.recv(1024).decode('utf-8')
client.close()

print(f"[Order Service Socket] Respons diterima: {response_data}")
