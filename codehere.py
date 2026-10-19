#yusufuma özel yapıldı
import time
tracks = "nigga" , "zenci" , "kömür" , "siyah" , "yusuf" , "yuse"
tracks1 = ["nigga" , "zenci" , "kömür" , "siyah" , "yusuf" , "yuse"]
while True: 
  a = str(input("okuldaki en yakisikli kisinin adini yaziniz      "))

  if a != "yusuf":
    print("yanliş  >:(")
    continue

  b = str(input("bu kişinin tüm adlarini bilmek istermisiniz?       "))
  c = str(input("bu kişinin adlarini hecelenmiş halini bilmek istermisiniz?      "))

  if a == "yusuf" and b == "evet" and c == "evet":
    for track in tracks1:
      print(track)
      for trackis in track:
        print(trackis)
  break
print("5 saniye sonra uygulama kapancak")
time.sleep(5)
