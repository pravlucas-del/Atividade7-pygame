"""
Módulo de Validações
Valida e-mail e força de senha
"""

def validar_email(email):
    """
    Valida um e-mail.
    O e-mail é válido quando termina com "@puc.com"
    
    Args:
        email (str): E-mail a ser validado
    
    Returns:
        bool: True se válido, False caso contrário
    
    (100XP)
    """
    if isinstance(email, str) and email.endswith("@puc.com"):
        return True
    return False


def validar_senha_segura(senha):
    """
    Valida se uma senha é segura/boa.
    
    Critérios:
    - Mínimo 8 caracteres
    - Pelo menos uma letra maiúscula
    - Pelo menos uma letra minúscula
    - Pelo menos um número
    
    Args:
        senha (str): Senha a ser validada
    
    Returns:
        bool: True se a senha é segura, False caso contrário
    
    (100XP)
    """
    if not isinstance(senha, str):
        return False
    
    # Verificar comprimento mínimo
    if len(senha) < 8:
        return False
    
    # Verificar se tem pelo menos uma letra maiúscula
    tem_maiuscula = any(c.isupper() for c in senha)
    
    # Verificar se tem pelo menos uma letra minúscula
    tem_minuscula = any(c.islower() for c in senha)
    
    # Verificar se tem pelo menos um número
    tem_numero = any(c.isdigit() for c in senha)
    
    return tem_maiuscula and tem_minuscula and tem_numero


# Testes das funções de validação
if __name__ == "__main__":
    print("=" * 50)
    print("TESTES DE VALIDAÇÃO")
    print("=" * 50)
    
    # Testes de e-mail
    print("\n--- Testes de E-mail ---")
    emails_teste = [
        ("joao@puc.com", True),
        ("maria@puc.com", True),
        ("admin@gmail.com", False),
        ("user@puc.br", False),
        ("@puc.com", True),  # Válido tecnicamente
    ]
    
    for email, esperado in emails_teste:
        resultado = validar_email(email)
        status = "✓" if resultado == esperado else "✗"
        print(f"{status} validar_email('{email}') = {resultado} (esperado: {esperado})")
    
    # Testes de senha
    print("\n--- Testes de Senha Segura ---")
    senhas_teste = [
        ("Senha123", True),      # Válida
        ("Abc12345", True),      # Válida
        ("senha123", False),     # Sem maiúscula
        ("SENHA123", False),     # Sem minúscula
        ("SenhaABC", False),     # Sem número
        ("Sen1", False),         # Muito curta
        ("SenhaSegura1", True),  # Válida
        ("A1b2c3d4", True),      # Válida
    ]
    
    for senha, esperado in senhas_teste:
        resultado = validar_senha_segura(senha)
        status = "✓" if resultado == esperado else "✗"
        print(f"{status} validar_senha_segura('{senha}') = {resultado} (esperado: {esperado})")
    
    print("\n" + "=" * 50)
