def somme_diviseurs(num):
    diviseurs = [i for i in range(1, num) if num % i == 0]
    return sum(diviseurs)

M = int(input("Entrez le premier entier M : "))
N = int(input("Entrez le deuxième entier N : "))

if somme_diviseurs(M) == N and somme_diviseurs(N) == M:
    print(f"{M} et {N} sont des amis.")
else:
    print(f"{M} et {N} ne sont pas amis.")
