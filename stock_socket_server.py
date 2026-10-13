import socket
import json
import sqlite3

DB_PATH = "/opt/toko-umkm/data/toko.db"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8002))
server.listen(5)
print("[Stock Service Socket] Server berjalan pada port 8002...")

while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode('utf-8')
    if data:
        req = json.loads(data)
        pid, qty = req["product_id"], req["qty"]

        db = sqlite3.connect(DB_PATH)
        cur = db.cursor()
        cur.execute("SELECT stok FROM produk WHERE id_produk = ?", (pid,))
        row = cur.fetchone()
        db.close()

        if not row:
            res = {"status": 404, "message": "Produk tidak ditemukan"}
        elif row[0] >= qty:
            res = {"status": 200, "message": "Stok mencukupi", "stok_sisa": row[0]}
        else:
            res = {"status": 409, "message": "Stok tidak mencukupi", "stok_sisa": row[0]}

        conn.send(json.dumps(res).encode('utf-8'))
    conn.close()
