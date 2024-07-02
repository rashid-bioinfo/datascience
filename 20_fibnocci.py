# fibnocci sequence

def feb():
    a, b = 0, 1
    while True:
        yield a
        a,b = b, a+b

print(f"feb: {feb()}")
for f in feb():
    if f > 50:
        break
    print(f)