import random
import string

def gerar_senha(tamanho):
    if tamanho < 6:
        print("Tente usar uma senha com pelo menos 6 caracteres para mais segurança.")
        return ""

    # Letras, números e símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Interface pelo terminal
print("=== Gerador de Senhas Seguras ===")
tamanho = int(input("Digite o comprimento desejado para a senha: "))
senha = gerar_senha(tamanho)

if senha:
    print(f"\nSenha gerada: {senha}")
