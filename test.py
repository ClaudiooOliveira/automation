import requests

# Substitua a URL abaixo pela URL do seu arquivo Python online
url_arquivo_py = "https://pastebin.com/qFq7Ppj1"

# Obter o conteúdo do arquivo online
try:
    resposta = requests.get(url_arquivo_py)
    resposta.raise_for_status()  # Lançar uma exceção para erros HTTP
    codigo_python = resposta.text
except requests.exceptions.RequestException as e:
    print(f"Erro ao obter o conteúdo do arquivo: {e}")
    codigo_python = None

# Imprimir o código Python antes de executar
print("Código Python a ser executado:")
print(codigo_python)

# Executar o código Python
if codigo_python is not None:
    try:
        exec(codigo_python)
    except Exception as e:
        print(f"Erro ao executar o código: {e}")
