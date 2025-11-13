login_correto = "aluno"
senha_correta = "1234"

print("=== SISTEMA DE LOGIN ESCOLAR ===")
print("Você tem 3 tentativas para acertar o login e a senha.\n")

tentativas = 3  # contador de tentativas

while tentativas > 0:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == login_correto and senha == senha_correta:
        print("\n✅ Login bem-sucedido! Bem-vindo(a),", login_correto, "!")
        break
    else:
        tentativas -= 1
        print("❌ Login ou senha incorretos.")
        if tentativas > 0:
            print(f"Você ainda tem {tentativas} tentativa(s). Tente novamente!\n")
        else:
            print("\n🚫 Suas tentativas acabaram! Acesso bloqueado.\n")

print("=== Fim do programa ===")