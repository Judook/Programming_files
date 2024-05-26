import keyboard

t = 0.0
asi = 0.0
aci = 0.0
si = 0.0
ci = 0.0
ad = 0.0
id = 0.0
sii = 0.0
cii = 0.0

p = float(input("Principal = Rs."))
r = float(input("Rate of interest = "))
t = float(input("Time in years : "))

keyboard.wait('F9')

asi = p
aci = p

keyboard.write('Time')
keyboard.press_and_release('right')
keyboard.write('ASI')
keyboard.press_and_release('right')
keyboard.write('SI')
keyboard.press_and_release('right')
keyboard.write('SII')
keyboard.press_and_release('right')
keyboard.write('ACI')
keyboard.press_and_release('right')
keyboard.write('CI')
keyboard.press_and_release('right')
keyboard.write('CII')
keyboard.press_and_release('right')
keyboard.write('AD')
keyboard.press_and_release('right')
keyboard.write('ID')
keyboard.press_and_release('down')
keyboard.press_and_release('Home')

for i in range(1, (int(t) + 1), 1) :
    sii = (r * p) / 100
    si = si + sii
    asi = asi + sii

    cii = (r * aci) / 100
    ci = ci + cii
    aci = aci + cii

    ad = aci - asi
    id = cii - sii

    asi = round(asi, 2)
    si = round(si, 2)
    sii = round(sii, 2)
    aci = round(aci, 2)
    ci = round(ci, 2)
    cii = round(cii, 2)
    ad = round(ad, 2)
    id = round(id, 2)
    
    keyboard.write(str(i))
    keyboard.press_and_release('right')
    keyboard.write(str(asi))
    keyboard.press_and_release('right')
    keyboard.write(str(si))
    keyboard.press_and_release('right')
    keyboard.write(str(sii))
    keyboard.press_and_release('right')
    keyboard.write(str(aci))
    keyboard.press_and_release('right')
    keyboard.write(str(ci))
    keyboard.press_and_release('right')
    keyboard.write(str(cii))
    keyboard.press_and_release('right')
    keyboard.write(str(ad))
    keyboard.press_and_release('right')
    keyboard.write(str(id))
    keyboard.press_and_release('down')
    keyboard.press_and_release('Home')
