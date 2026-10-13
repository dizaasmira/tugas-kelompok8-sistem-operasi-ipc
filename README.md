#### Implementasi Inter-Process Communication (IPC) & Sistem Operasi

Repository tugas kelompok mata kuliah *Sistem Operasi* (Modul TI-3D & K-1D).
Proyek ini mendemonstrasikan komunikasi antar-proses (*Inter-Process Communication* / IPC) menggunakan dua pendekatan berbeda—*XML-RPC* dan *Socket TCP*—yang terhubung dengan database lokal SQLite pada lingkungan Ubuntu Server 26.04.


 ## Lingkungan & Spesifikasi Sistem
 
 **Sistem Operasi:** Ubuntu Server 26.04 (`srv-toko-250660121024`)
 
 **Bahasa Pemrograman:** Python 3
 
 **Database:** SQLite (`/opt/toko-umkm/data/toko.db`)
 
**Tabel Utama:** `produk` (kolom: `id_produk`, `nama_produk`, `stok`, `harga`)



## Struktur Berkas Repository

| `stock_rpc_server.py`    | Server stok backend berbasis XML-RPC      | HTTP / Port `8001`

| `order_rpc_client.py`    | Client pemesanan untuk menguji XML-RPC    | XML-RPC Client  

| `stock_socket_server.py` | Server stok backend berbasis Socket TCP   | TCP Stream / Port `8002` 

| `order_socket_client.py` | Client pemesanan untuk menguji Socket TCP | JSON over TCP            


## Panduan Menjalankan Program & Pengujian

### A. Pengujian Layanan XML-RPC (Port 8001) & Pengujian Layanan Socket TCP (Port 8002)

1. **Jalankan Server (Terminal 1):**
   ```bash
   python3 stock_rpc_server.py #untuk pengujian rpc
   python3 stock_socket_server.py #untuk pengujian socket tpc
    
2. **Jalankan Client untuk Skenario Pengujian (Terminal 2):**


   ```bash
   python3 order_rpc_client.py P001 1 #Skenario 1 - Stok Cukup (Produk P001, Beli 1)
   python3 order_rpc_client.py P999 25 #Skenario 2 - Stok Tidak Mencukupi (Produk P999, Beli 25)
   python3 order_rpc_client.py P9999 1 #Skenario 3 - Produk Tidak Ditemukan (Produk P9999, Beli 1)
