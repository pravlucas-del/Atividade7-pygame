def hexagonos(n):
    return 3 * n * (n - 1) + 1

def hexagonos_rec(n):
    if n == 1:
        return 1
    else:
        return hexagonos_rec(n-1) + 6 * (n-1)

def quadrados(n):
    return n**2

def quadrados_rec(n):
    if n == 1:
        return 1
    else:
        return quadrados_rec(n-1) + 4 * (n-1)

def triangulos(n):
    return (3 * n**2 - 3 * n + 2) // 2

def triangulos_rec(n):
    if n == 1:
        return 1
    else:
        return triangulos_rec(n-1) + 3 * (n-1)

def main():
    
    m = int(input("Digite um número natural m: "))

    hexagonos_list = [hexagonos_rec(i) for i in range(1, m+1)]
    quadrados_list = [quadrados_rec(i) for i in range(1, m+1)]
    triangulos_list = [triangulos_rec(i) for i in range(1, m+1)]

    print("Sequência de hexágonos:", hexagonos_list)
    print("Sequência de quadrados:", quadrados_list)
    print("Sequência de triângulos:", triangulos_list)

    comuns_hex_quad = set(hexagonos_list) and set(quadrados_list)
    comuns_hex_triang = set(hexagonos_list) and set(triangulos_list)
    comuns_quad_triang = set(quadrados_list) and set(triangulos_list)

    print("Termos comuns entre hexágonos e quadrados:", comuns_hex_quad)
    print("Termos comuns entre hexágonos e triângulos:", comuns_hex_triang)
    print("Tremos comuns entre quadrados e triângulos:", comuns_quad_triang)

print("Bem_vindo ao programa de contagem de azulejos!")
main()

print(hexagonos(5))
print(quadrados(5))
print(triangulos(5))