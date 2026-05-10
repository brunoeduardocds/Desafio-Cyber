import os
from cryptography.fernet import Fernet

# 1. Carregar a chave que foi gerada pelo encrypter
try:
    with open("chave.key", "rb") as key_file:
        chave = key_file.read()
except FileNotFoundError:
    print("Erro: O arquivo 'chave.key' não foi encontrado. Não é possível descriptografar.")
    exit()

# 2. Inicializar o Fernet com a chave carregada
fernet = Fernet(chave)

# 3. Localizar os arquivos na pasta de teste
caminho_alvo = "arquivos_teste"
arquivos = [f for f in os.listdir(caminho_alvo) if os.path.isfile(os.path.join(caminho_alvo, f))]

print(f"Restaurando arquivos em: {caminho_alvo}...")

for nome_arquivo in arquivos:
    caminho_completo = os.path.join(caminho_alvo, nome_arquivo)
    
    # Ler os dados criptografados
    with open(caminho_completo, "rb") as arquivo:
        dados_criptografados = arquivo.read()
    
    try:
        # Descriptografar os dados
        dados_originais = fernet.decrypt(dados_criptografados)
        
        # Sobrescrever o arquivo com os dados originais
        with open(caminho_completo, "wb") as arquivo:
            arquivo.write(dados_originais)
        print(f"Sucesso: {nome_arquivo} restaurado.")
    except Exception as e:
        print(f"Erro ao descriptografar {nome_arquivo}: Talvez ele não esteja criptografado ou a chave está incorreta.")

print("\nProcesso de restauração finalizado!")