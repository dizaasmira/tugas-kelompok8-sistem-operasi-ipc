import xmlrpc.client
import sys

# Membuka koneksi RPC ke Stock Service
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:8001/")

# Menerima parameter dari command line (default: P001 dan qty 1)
product_id = sys.argv[1] if len(sys.argv) > 1 else "P001"
qty = int(sys.argv[2]) if len(sys.argv) > 2 else 1

print(f"[Order Service] Mengirim RPC check_stock({product_id}, {qty})...")
response = proxy.check_stock(product_id, qty)
print(f"[Order Service] Respons dari Stock Service: {response}")
