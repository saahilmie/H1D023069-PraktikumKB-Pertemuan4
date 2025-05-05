import requests
import json

def konversi_mata_uang(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching data from API")
        return None
    
    data = response.json()
    return data['rates'].get(target_currency)

def convert_currency(amount, rate):
    return amount * rate

def main():
    print("Halo, kamu bisa mengonversi mata uang di sini ya!")
    base_currency = input("Masukkan mata uang dasar (misal: USD): ").upper()
    target_currency = input("Masukkan mata uang target (misal: IDR): ").upper()
    amount = float(input("Masukkan jumlah yang ingin dikonversi: "))
    
    rate = konversi_mata_uang(base_currency, target_currency)
    
    if rate:
        converted_amount = convert_currency(amount, rate)
        print(f"{amount} {base_currency} sama dengan {converted_amount:.2f} {target_currency}.")
    else:
        print("Konversi gagal. Mata uang tidak ditemukan.")

if __name__ == "__main__":
    main()
