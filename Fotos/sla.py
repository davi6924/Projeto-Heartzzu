import os

# Caminho da pasta com as imagens
pasta = "."

# Extensões de imagens suportadas
extensoes = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']

# Lista de arquivos de imagem
imagens = [f for f in os.listdir(pasta) if os.path.splitext(f)[1].lower() in extensoes]

# Ordena a lista para garantir ordem consistente
imagens.sort()

# Renomeia as imagens
for i, nome_original in enumerate(imagens, start=1):
    extensao = os.path.splitext(nome_original)[1]
    novo_nome = f"img{i}{extensao}"
    caminho_antigo = os.path.join(pasta, nome_original)
    caminho_novo = os.path.join(pasta, novo_nome)
    os.rename(caminho_antigo, caminho_novo)
    print(f"{nome_original} → {novo_nome}")
