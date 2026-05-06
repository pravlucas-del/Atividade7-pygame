# ==========================================
# ATIVIDADE 8 - VALIDAÇÕES
# ==========================================
# Função para validar e-mail (100XP)
# Função para validar senha segura (100XP)

def validar_email(email):
    """
    Valida se um e-mail termina com '@puc.com'
    
    Args:
        email (str): E-mail a ser validado
        
    Returns:
        bool: True se válido, False caso contrário
    """
    return isinstance(email, str) and email.endswith("@puc.com")


def validar_senha_segura(senha):
    """
    Valida se uma senha é segura (boa).
    
    Critérios:
    - Mínimo 8 caracteres
    - Pelo menos 1 letra maiúscula
    - Pelo menos 1 letra minúscula
    - Pelo menos 1 número
    
    Args:
        senha (str): Senha a ser validada
        
    Returns:
        bool: True se a senha é segura, False caso contrário
    """
    if not isinstance(senha, str):
        return False
    
    # Validação de comprimento
    if len(senha) < 8:
        return False
    
    # Validação de letra maiúscula
    tem_maiuscula = any(char.isupper() for char in senha)
    if not tem_maiuscula:
        return False
    
    # Validação de letra minúscula
    tem_minuscula = any(char.islower() for char in senha)
    if not tem_minuscula:
        return False
    
    # Validação de número
    tem_numero = any(char.isdigit() for char in senha)
    if not tem_numero:
        return False
    
    return True


# ==========================================
# TESTES
# ==========================================
if __name__ == "__main__":
    print("=" * 50)
    print("TESTES DE VALIDAÇÃO")
    print("=" * 50)
    
    # Testes de E-mail
    print("\n--- TESTES DE E-MAIL ---")
    emails_teste = [
        ("user@puc.com", True),
        ("admin@puc.com", True),
        ("teste@gmail.com", False),
        ("aluno@puc.br", False),
        ("invalido@puc.co", False),
    ]
    
    for email, esperado in emails_teste:
        resultado = validar_email(email)
        status = "✓" if resultado == esperado else "✗"
        print(f"{status} Email: {email} -> {resultado} (esperado: {esperado})")
    
    # Testes de Senha
    print("\n--- TESTES DE SENHA SEGURA ---")
    senhas_teste = [
        ("Senha123", True),           # Válida
        ("Abc12345", True),           # Válida
        ("senha123", False),          # Sem maiúscula
        ("SENHA123", False),          # Sem minúscula
        ("Senha", False),             # Sem número
        ("Senha1", False),            # Menos de 8 caracteres
        ("SenhaSegura1", True),       # Válida
        ("12345678", False),          # Só números
        ("Abc", False),               # Muito curta
    ]
    
    for senha, esperado in senhas_teste:
        resultado = validar_senha_segura(senha)
        status = "✓" if resultado == esperado else "✗"
        print(f"{status} Senha: {senha:20} -> {resultado:5} (esperado: {esperado})")
    
    print("\n" + "=" * 50)
