# Corporate WA Flow 💼📱

Este repositório contém uma automação em Python para o envio de comunicados internos via WhatsApp Web utilizando o Microsoft Edge. O foco principal é manter uma cadência de disparos segura para evitar bloqueios.

## 🛡️ Estratégia de Segurança (Anti-Ban)

O script implementa uma técnica de "aquecimento" e repouso para simular o uso humano:
- **Intervalo Individual:** Pausa de 15 segundos entre cada mensagem.
- **Lotes (Batches):** Envia para 25 contatos por vez.
- **Repouso Curto:** Pausa de **1 hora** após cada lote de 25 envios.
- **Ciclo de Segurança:** Após concluir 4 lotes (100 mensagens), o sistema entra em **Repouso Estendido por 24 horas**.

## 🚀 Funcionalidades
- **Persistência de Dados:** Salva os números já contatados em um arquivo `contacted_numbers.json`, garantindo que ninguém receba a mesma mensagem duas vezes em caso de reinicialização.
- **Automação via Edge:** Utiliza o navegador Microsoft Edge para maior compatibilidade em ambientes corporativos Windows.

## 🛠️ Tecnologias
- Python 3.x
- Selenium
- Edge WebDriver

## 📋 Como configurar o código
1. No arquivo principal, localize a variável `driver_path` e insira o caminho do seu `msedgedriver.exe`.
2. Adicione os números na lista `numbers_to_contact` no formato internacional (ex: `5511999998888`).
3. Personalize sua mensagem na variável `message`.

## ⚠️ Observação Importante
Certifique-se de que o seu **Edge WebDriver** é da mesma versão que o seu navegador Microsoft Edge instalado.
