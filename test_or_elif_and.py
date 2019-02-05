quieres_el_auto_ses = input("¿quieres el auto?: ")
tienes_dinero_ses = input("¿tienes dinero para pagarlo?: ")
senor_auto_ses = input("¿está el senor que te lo ba a vender?: ")
esta_el_auto_ses = input("¿está el auto que quieres?: ")
te_presto_ses = input("¿te presto dinero?: ")

if te_presto_ses == "si":
    te_presto = True
elif te_presto_ses == "no":
    te_presto = False
else:
    print("i asked you something that should answer me with yer or no, i think you said no")

quieres_el_auto = quieres_el_auto_ses == "si"
tienes_dinero = tienes_dinero_ses == "si"
senor_auto = senor_auto_ses == "si"
esta_el_auto = esta_el_auto_ses == "si"
te_presto = te_presto_ses == "si"

if quieres_el_auto and (tienes_dinero or te_presto) and senor_auto and esta_el_auto:
    print("let's buy it")
else:
    print("okay, not today")