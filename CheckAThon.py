_author_ = 'RgAKH5'
#Skrip pengecek teks


inp = list(input("Masukkan teks apapun(OPSIONAL)..:\n"))
simb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890-©®/:;€&@.,?!#%^*+=_\|~<>$£¥•)"
num = 0

for let in list(simb):
  num = 0
  for letters in inp:
    if letters == let:
      num += 1
  print(let, ":", num)