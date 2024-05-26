def biner_ke_teks(biner):
    biner_list = biner.split(' ')
    teks = ''.join([chr(int(b, 2)) for b in biner_list])
    return teks

biner = "01000001 01100100 01100001 00100000 01110010 01100001 01110100 01110101 01110011 01100001 01101110 00100000 01110011 01100101 01100010 01100001 01100010 00100000 01101101 01100101 01101110 01100111 01100001 01110000 01100001 00100000 01100001 01101011 01110101 00100000 01101000 01100001 01110010 01110101 01110011 00100000 01101101 01100101 01101110 01101010 01100001 01110101 01101000 01101001 01101101 01110101 00101110 00100000 00001010 01001110 01100001 01101101 01110101 01101110 00100000 01101101 01100101 01101110 01100100 01100101 01101011 01100001 01110100 01101001 01101101 01110101 00100000 01100001 01101011 01110101 00100000 01101000 01100001 01101110 01111001 01100001 00100000 01101101 01100101 01101101 01101001 01101100 01101001 01101011 01101001 00100000 01110100 01101001 01100111 01100001 00100000 01110011 01100101 01100010 01100001 01100010 00111010 00001010 00110001 00101110 00100000 01101011 01100001 01110010 01100101 01101110 01100001 00100000 01110100 01101001 01100100 01100001 01101011 00100000 01110011 01100101 01101110 01100111 01100001 01101010 01100001 00100000 01100010 01100101 01110010 01110100 01100101 01101101 01110101 00101100 00001010 00110010 00101110 00100000 01101011 01100001 01110010 01100101 01101110 01100001 00100000 01100001 01100100 01100001 00100000 01110000 01100101 01110010 01101100 01110101 00101100 00001010 00110011 00101110 00100000 01100001 01110100 01100001 01110101 00100000 01101011 01100001 01110010 01100101 01101110 01100001 00100000 01101001 01101110 01100111 01101001 01101110 00100000 01101101 01100101 01101110 01100001 01101110 01111001 01100001 01101011 01100001 01101110 00100000 01101011 01100001 01100010 01100001 01110010 00101110"

perintah = input("Masukkan perintah(Ketik 'terjemahkan'): ")
if perintah.lower() == "terjemahkan":
    teks = biner_ke_teks(biner)
    print(teks)
else:
    print("Perintah tidak dikenali.")
    


import turtle

turtle.penup ()
turtle.left (90)
turtle.fd (200)
turtle.pendown ()
turtle.right (90)
 
turtle.fillcolor ("red")
turtle.begin_fill ()
turtle.circle (10,180)
turtle.circle (25,110)
turtle.left (50)
turtle.circle (60,45)
turtle.circle (20,170)
turtle.right (24)
turtle.fd (30)
turtle.left (10)
turtle.circle (30,110)
turtle.fd (20)
turtle.left (40)
turtle.circle (90,70)
turtle.circle (30,150)
turtle.right (30)
turtle.fd (15)
turtle.circle (80,90)
turtle.left (15)
turtle.fd (45)
turtle.right (165)
turtle.fd (20)
turtle.left (155)
turtle.circle (150,80)
turtle.left (50)
turtle.circle (150,90)
turtle.end_fill ()
 
turtle.left (150)
turtle.circle (-90,70)
turtle.left (20)
turtle.circle (75,105)
turtle.setheading (60)
turtle.circle (80,98)
turtle.circle (-90,40)
 
turtle.left (180)
turtle.circle (90,40)
turtle.circle (-80,98)
turtle.setheading (-83)
 
turtle.fd (30)
turtle.left (90)
turtle.fd (25)
turtle.left (45)
turtle.fillcolor ("green")
turtle.begin_fill ()
turtle.circle (-80,90)
turtle.right (90)
turtle.circle (-80,90)
turtle.end_fill ()
turtle.right (135)
turtle.fd (60)
turtle.left (180)
turtle.fd (85)
turtle.left (90)
turtle.fd (80)
 
turtle.right (90)
turtle.right (45)
turtle.fillcolor ("green")
turtle.begin_fill ()
turtle.circle (80,90)
turtle.left (90)
turtle.circle (80,90)
turtle.end_fill ()
turtle.left (135)
turtle.fd (60)
turtle.left (180)
turtle.fd (60)
turtle.right (90)
turtle.circle (200,60)

turtle.done()
