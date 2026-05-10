# 🛡️ Cybersecurity Challenge: Malware Simulation with Python

Este projeto foi desenvolvido como parte de um desafio prático de cibersegurança. O objetivo é compreender, de forma técnica e em ambiente controlado, o funcionamento de duas ameaças comuns: **Ransomware** e **Keylogger**.

> **⚠️ AVISO:** Este projeto possui fins estritamente educativos e deve ser utilizado apenas em ambientes de teste controlados.

## 📁 Estrutura do Projeto

* `/ransomware`: Contém scripts para simular a criptografia de arquivos.
    * `encrypter.py`: Cifra os arquivos usando a biblioteca `cryptography`.
    * `decrypter.py`: Restaura os arquivos originais utilizando a chave gerada.
* `/keylogger`: Contém o script de monitoramento de teclado.
    * `keylogger.py`: Captura as teclas digitadas e armazena em um log local.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas:** * `cryptography` (Criptografia simétrica Fernet)
    * `pynput` (Monitoramento de periféricos)
    * `logging` (Registro de eventos)

## 🚀 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```
2.  **Instale as dependências:**
    ```bash
    pip install cryptography pynput
    ```
3.  **Para testar o Ransomware:**
    * Coloque arquivos de teste na pasta `arquivos_teste`.
    * Execute `python ransomware/encrypter.py`.
    * Para restaurar, execute `python ransomware/decrypter.py`.
4.  **Para testar o Keylogger:**
    * Execute `python keylogger/keylogger.py`.
    * Digite e pressione `Esc` para finalizar. Confira o arquivo `keylog.txt`.

## 🛡️ Reflexão sobre Defesa e Prevenção

A melhor forma de se proteger contra essas ameaças no mundo real inclui:
1.  **Backups Offline:** Manter cópias de segurança fora da rede principal para mitigar ataques de Ransomware.
2.  **Antivírus/EDR:** Ferramentas que monitoram comportamentos suspeitos (como a criação rápida de arquivos cifrados).
3.  **Higiene Digital:** Evitar a execução de scripts ou anexos de fontes desconhecidas que possam instalar Keyloggers em segundo plano.