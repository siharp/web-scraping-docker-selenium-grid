import multiprocessing
from script import batik, lion, saj, merge_json
import os
from dotenv import load_dotenv

load_dotenv()  # Memuat variabel lingkungan dari file .env jika ada
username = os.getenv('user_name')
password = os.getenv('password')
start_date = '2025-05-01'  # Ganti dengan tanggal mulai yang diinginkan
end_date = '2025-05-31'  # Ganti dengan tanggal akhir yang diinginkan

def run_batik():
    batik.main_batik(username=username, password=password, start_date=start_date, end_date=end_date)

def run_lion():
    lion.main_lion(username=username, password=password, start_date=start_date, end_date=end_date)

def run_saj():
    saj.main_saj(username=username, password=password, start_date=start_date, end_date=end_date)



if __name__ == "__main__":
    # Membuat dan menjalankan proses secara paralel
    processes = []

    # Menambahkan setiap proses
    processes.append(multiprocessing.Process(target=run_batik))
    processes.append(multiprocessing.Process(target=run_lion))
    processes.append(multiprocessing.Process(target=run_saj))
    

    # Memulai semua proses
    for p in processes:
        p.start()

    # Menunggu semua proses selesai
    for p in processes:
        p.join()

    print("Semua skrip telah selesai dijalankan.")

    # Menggabungkan file JSON menjadi CSV
    merge_json.process_json_to_csv('./data', '.')