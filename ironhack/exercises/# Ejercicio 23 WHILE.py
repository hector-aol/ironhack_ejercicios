# Ejercicio 23 WHILE

a, p, n = "pan", "55.865", "1230"

e, d = "", ""
ve = False
i = 0
while i < len(p):
    k = p[i]
    if k != "." and not ve:
        e += k
    else:
        if k == "." and not ve:
            ve = True
        else:
            d += k
    i += 1

# Rellenar o cortar e a 6 dígitos
while len(e) < 6:
    e = '0' + e
if len(e) > 6:
    e = e[:6]

# Rellenar o cortar d a 2 dígitos
if len(d) < 2:
    d = d + "0"
elif len(d) > 2:
    d = d[:2]

# Formatear n a 3 dígitos
if len(n) < 3:
    n = '0' * (3 - len(n)) + n
elif len(n) > 3:
    n = n[:3]

ep, dp = e, d

# Multiplicación
c = str(float(p) * int(float(n)))

e, d = "", ""
ve = False
i = 0
while i < len(c):
    k = c[i]
    if k != "." and not ve:
        e += k
    else:
        if k == "." and not ve:
            ve = True
        else:
            d += k
    i += 1

# Rellenar o cortar e a 8 dígitos
while len(e) < 8:
    e = '0' + e
if len(e) > 8:
    e = e[:8]

# Rellenar o cortar d a 2 dígitos
if len(d) < 2:
    d = d + "0"
elif len(d) > 2:
    d = d[:2]

ec, dc = e, d

print(f"{ep}.{dp} * {n} = {ec}.{dc}")