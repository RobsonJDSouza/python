#beecrowd
p1, np1, vlp1 = input().split(" ")
p2, np2, vlp2 = input().split(" ")

p1 = int(p1)
np1 = int(np1)
vlp1 = float(vlp1)

p2 = int(p2)
np2 = int(np2)
vlp2 = float(vlp2)

soma = (np1* vlp1) + (np2*vlp2)
print(f"VALOR A PAGAR: R$ {soma:.2f}")