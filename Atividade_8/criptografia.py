"""
Módulo de Criptografia com Cifra de César
Implementa criptografia e descriptografia com deslocamento de +3
"""

def criptografar_cesar(texto, deslocamento=3):
    """
    Criptografa um texto usando a Cifra de César.
    
    Características:
    - Válidos: caracteres ASCII entre '0' (48) e 'z' (122)
    - Deslocamento padrão: +3
    - Mantém caracteres fora do intervalo sem alteração
    
    Args:
        texto (str): Texto a ser criptografado
        deslocamento (int): Deslocamento na tabela ASCII (padrão: 3)
    
    Returns:
        str: Texto criptografado
    
    (300XP - Parte 1)
    """
    texto_criptografado = ""
    
    for char in texto:
        # Obter valor ASCII do caractere
        ascii_value = ord(char)
        
        # Intervalo válido: '0' (48) até 'z' (122)
        if 48 <= ascii_value <= 122:
            # Calcular novo valor com deslocamento
            novo_valor = ascii_value + deslocamento
            
            # Se ultrapassar o limite superior, volta ao início
            if novo_valor > 122:
                novo_valor = 48 + (novo_valor - 123)
            
            # Converter para caractere
            texto_criptografado += chr(novo_valor)
        else:
            # Caracteres fora do intervalo mantêm-se iguais
            texto_criptografado += char
    
    return texto_criptografado


def descriptografar_cesar(texto, deslocamento=3):
    """
    Descriptografa um texto criptografado com Cifra de César.
    
    Funciona de forma inversa à criptografia, subtraindo o deslocamento.
    
    Args:
        texto (str): Texto criptografado a ser descriptografado
        deslocamento (int): Deslocamento usado na criptografia (padrão: 3)
    
    Returns:
        str: Texto original (descriptografado)
    
    (50XP - EXTRA)
    """
    texto_descriptografado = ""
    
    for char in texto:
        # Obter valor ASCII do caractere
        ascii_value = ord(char)
        
        # Intervalo válido: '0' (48) até 'z' (122)
        if 48 <= ascii_value <= 122:
            # Calcular novo valor com deslocamento inverso
            novo_valor = ascii_value - deslocamento
            
            # Se ultrapassar o limite inferior, volta ao final
            if novo_valor < 48:
                novo_valor = 122 - (47 - novo_valor)
            
            # Converter para caractere
            texto_descriptografado += chr(novo_valor)
        else:
            # Caracteres fora do intervalo mantêm-se iguais
            texto_descriptografado += char
    
    return texto_descriptografado


# Testes das funções de criptografia
if __name__ == "__main__":
    print("=" * 70)
    print("TESTES DE CRIPTOGRAFIA E DESCRIPTOGRAFIA - CIFRA DE CÉSAR")
    print("=" * 70)
    
    # Testes básicos
    print("\n--- Testes Básicos (Deslocamento +3) ---")
    testes = [
        "senha123",
        "Abc12345",
        "python",
        "123xyz",
        "0123456789",
        "abcdefghijklmnopqrstuvwxyz",
    ]
    
    for texto_original in testes:
        criptografado = criptografar_cesar(texto_original)
        descriptografado = descriptografar_cesar(criptografado)
        
        # Verificar se descriptografia retorna ao original
        sucesso = "✓" if descriptografado == texto_original else "✗"
        
        print(f"\n{sucesso} Original:        {texto_original}")
        print(f"  Criptografado:  {criptografado}")
        print(f"  Descriptografado: {descriptografado}")
    
    # Teste de caracteres especiais
    print("\n\n--- Teste com Caracteres Especiais ---")
    texto_especial = "senha@123"
    cripto_especial = criptografar_cesar(texto_especial)
    descripto_especial = descriptografar_cesar(cripto_especial)
    
    print(f"Original:          {texto_especial}")
    print(f"Criptografado:     {cripto_especial}")
    print(f"Descriptografado:  {descripto_especial}")
    print(f"Mantém '@': {('@' in cripto_especial and '@' in descripto_especial)}")
    
    # Teste de limite da tabela ASCII
    print("\n\n--- Teste de Limite (Wrapping) ---")
    limite_texto = "xyz"
    cripto_limite = criptografar_cesar(limite_texto)
    descripto_limite = descriptografar_cesar(cripto_limite)
    
    print(f"Original:          {limite_texto}")
    print(f"Criptografado:     {cripto_limite}")
    print(f"Descriptografado:  {descripto_limite}")
    print(f"Valores ASCII: {[ord(c) for c in limite_texto]} -> {[ord(c) for c in cripto_limite]}")
    
    # Teste com deslocamento customizado
    print("\n\n--- Teste com Deslocamento Customizado (+5) ---")
    texto_custom = "teste"
    cripto_custom = criptografar_cesar(texto_custom, deslocamento=5)
    descripto_custom = descriptografar_cesar(cripto_custom, deslocamento=5)
    
    print(f"Original:          {texto_custom}")
    print(f"Criptografado (+5): {cripto_custom}")
    print(f"Descriptografado:  {descripto_custom}")
    
    print("\n" + "=" * 70)
