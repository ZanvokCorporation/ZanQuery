import os

print("ZanQuery Activation - Install Product Key")
print()
pkey = ""
while pkey != "exit":
    pkey = input("Enter you 3-digit Product Key: ").upper()
    print()
    if pkey == "TP" or pkey == "TP1" or pkey == "TP2" or pkey == "TP3" or pkey == "TP4" or pkey == "TP5":
        print("This Product Key Works....")
        cont = input("Press any key to continue..")
        file = open("C:/ZanQuery/Data/Activation/activation.dat","a")
        file.write(pkey)
        file.close()
        print("Product Key Installed")
        quit_prompt = input("Press any key to exit...")
        break
    else:
        print("Invalid Product Key...")
        
