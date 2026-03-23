import socket

target_ip = input("Enter the target IP: ")
print("Scanning ports 1 to 10000...")       

for port in range(1, 65536):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
       # Yeni bir TCP socket oluşturur (AF_INET = IPv4, SOCK_STREAM = TCP)
    # "with" bloğu sayesinde işlem bitince socket otomatik kapanır
    sck.settimeout(0.0000000000001)
      # Bağlantı denemesi için maksimum bekleme süresini 0.5 saniye yapar
    

    result = sck.connect_ex((target_ip, port))
   # Belirtilen IP ve porta bağlanmayı dener
        # Hata fırlatmaz, bunun yerine sonuç kodu döner
        # 0 dönerse bağlantı başarılı (port açık), diğer değerler başarısız

    if result == 0: # Eğer sonuç 0 ise yani bağlantı kurulmuşsa
          try:
                srv = socket.getservbyport(port)
          except:
                srv = "unknown"
 
       
          print(f"-> {port} is open|Service:{srv}")
            # Açık olan port numarasını ekrana yazdırır
print("Scan completed")
