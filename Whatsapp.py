from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import time

# Caminho para o WebDriver do Edge
driver_path = r 'C:\Path\To\Your\msedgedriver.exe'  # Altere para o caminho correto do seu WebDriver

# Configuração do Edge
options = Options()
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=options)

# Acessa o WhatsApp Web
driver.get('https://web.whatsapp.com')

# Pausa para escanear o QR code
input("Pressione Enter após escanear o QR code")

print("QR code escaneado com sucesso! Preparando para enviar mensagens...")

# Lista de números para contatar (formato internacional)
numbers_to_contact = []
contacted_numbers = set()

# Caminho para o arquivo JSON
json_file_path = os.path.join(os.getcwd(), 'contacted_numbers.json')

# Carregar números já contatados de um arquivo, se existir
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as file:
        contacted_numbers = set(json.load(file))
else:
    # Inicializa o arquivo JSON se não existir
    with open(json_file_path, 'w') as file:
        json.dump([], file)

def send_message(number, message):
    try:
        # Abre diretamente a conversa no WhatsApp Web com o número
        driver.get(f'https://web.whatsapp.com/send?phone={number}')

        # Espera a página carregar e o campo de mensagem estar disponível
        WebDriverWait(driver, 45).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
        
        # Envia a mensagem
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.click()
        message_box.send_keys(message)
        time.sleep(15)  # Pequena pausa para evitar erros de timing
        message_box.send_keys(Keys.ENTER)

        print(f'Mensagem enviada para: {number}')
        contacted_numbers.add(number)  # Adiciona à lista de contatos enviados

        # Salvar números contatados no arquivo após cada envio
        with open(json_file_path, 'w') as file:
            json.dump(list(contacted_numbers), file)

    except Exception as e:
        print(f'Erro ao enviar para {number}: {e}')

# Mensagem com link interativo
message = (
    "Olá! Gostaria de compartilhar um link interessante com você: "
    "https://www.exemplo.com "
    "Clique no link para mais informações!"
)

# Configurações para o envio em lotes
batch_size = 25  # Tamanho do lote
total_batches = 4  # Número de lotes antes da pausa de 24 horas

for i in range(0, len(numbers_to_contact), batch_size):
    batch = numbers_to_contact[i:i + batch_size]
    
    for number in batch:
        if number not in contacted_numbers:
            send_message(number, message)
            time.sleep(15)  # Pausa de 15 segundos após cada envio

    # Pausa de 1 hora após cada lote de 25 mensagens
    print(f"Pausa de 1 hora após o envio de {i + batch_size} mensagens.")
    time.sleep(3600)  # 1 hora em segundos

    # Após enviar 4 lotes, faça uma pausa de 24 horas
    if (i // batch_size + 1) % total_batches == 0:
        print("Pausando por 24 horas após 4 lotes.")
        time.sleep(86400)  # 24 horas em segundos

driver.quit()