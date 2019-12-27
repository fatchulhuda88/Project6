
from view.view_nilai import search,cetak,header,notoption
from view.input_nilai import inputan,edit,delete
header()
while True:

    c = input("\nPilih Opsi: ")

    # EXIT PROGRAM
    if c.lower() == 'q':
        print(".:TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI:.")
        ext = input("\nPress ENTER to exit")
        if ext == '':
            break
        else:
            break

    # PRINT DATA
    elif c.lower() == 'l':
        cetak()

    # MENAMBAH DATA
    elif c.lower() == 'a':
        inputan()

    # EDIT DATA
    elif c.lower() == 'e':
        edit()

    # MENCARI DATA
    elif c.lower() == 's':
        search()

    # HAPUS DATA
    elif c.lower() == 'd':
        delete()

    else:
        notoption()