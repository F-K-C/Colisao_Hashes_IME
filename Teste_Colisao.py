import hashlib

def calcular_hash(arquivo):
    with open(arquivo, "rb") as f:
        dados = f.read()
    ArquivoHash = hashlib.md5(dados)
    return ArquivoHash.hexdigest()

OutroArquivoHashAviao = calcular_hash("images/plane.jpeg")
OutroArquivoHashNavio = calcular_hash("images/ship.jpeg")

print("O Arquivo Hash do avião é: ", OutroArquivoHashAviao)
print("O Arquivo Hash do navio é: ", OutroArquivoHashNavio)

if OutroArquivoHashNavio == OutroArquivoHashAviao:
    print("Colisão Detectada!")
else:
    print("Sem colisões, Hashes diferentes!!")