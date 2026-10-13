from xmlrpc.server import SimpleXMLRPCServer
import sqlite3

DB_PATH = "/opt/toko-umkm/data/toko.db"

def check_stock(product_id, quantity):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Menggunakan 'id_produk' sesuai struktur tabel SQLite
    cursor.execute("SELECT stok FROM produk WHERE id_produk = ?", (product_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return {"status": 404, "message": "Produk tidak ditemukan"}

    current_stock = row[0]
    if current_stock >= quantity:
        return {"status": 200, "message": "Stok mencukupi", "stok_sisa": current_stock}
    else:
        return {"status": 409, "message": "Stok tidak mencukupi", "stok_sisa": current_stock}

server = SimpleXMLRPCServer(("127.0.0.1", 8001), allow_none=True)
print("[Stock Service XML-RPC] Server berjalan pada port 8001...")
server.register_function(check_stock, "check_stock")
server.serve_forever()
