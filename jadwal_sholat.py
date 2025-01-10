import requests
from datetime import datetime



    #REQUEST LATITUDE & LONGITUDE KOTA 
def get_lat_lon_kota():

    # INPUT NAMA KOTA
    kota = input("Masukkan Nama Kota:")

    #  URL API dengan parameter pencarian
    url = "https://nominatim.openstreetmap.org/search?city={kota}&format=json"
    
    # Header dengan User-Agent untuk identifikasi klien
    headers = {"User-Agent": "chrome"}
    
     # Mengirim permintaan GET ke API
    response = requests.get(url, headers=headers)
    
    # mMemastikan respons HTTP berhasil
    response.raise_for_status()
    
    # Mengubah respons JSON ke struktur data Python
    data = response.json()
    
    # Mengambil nilai latitude dan longitude dari respons JSON
    lat = data[0]['lat']
    lon = data[0]['lon']

    # URL API untuk mendapatkan jadwal waktu sholat
    url = f"https://api.aladhan.com/v1/timings?latitude={lat}&longitude={lon}&method=2"
    headers = {"User-Agent": "chrome"}   
    # Mengirim permintaan
    response = requests.get(url, headers=headers)
    response.raise_for_status()
        
    # Mengubah respons JSON
    data = response.json()
        
    # Mengambil jadwal waktu sholat dari respons JSON
    timings = data['data']['timings']
    # Tag Waktu
    subuh = timings['Fajr']
    dzuhur = timings['Dhuhr']
    ashar = timings['Asr']
    maghrib = timings['Maghrib']
    isya = timings['Isha']


    # Tampilan waktu sholat
    print(f"Subuh: {subuh} AM")
    print(f"Dzuhur: {dzuhur} PM")
    print(f"Ashar: {ashar} PM")
    print(f"Maghrib: {maghrib} PM")
    print(f"Isya: {isya} PM")
#Program urut
get_lat_lon_kota()
#  menggulangi lagi
back =input("inggin kembali/ganti kota? (y/n):")
if back == "y":
    get_lat_lon_kota()
elif back == "n":
    print("Terima kasih telah menggunakan program ini")