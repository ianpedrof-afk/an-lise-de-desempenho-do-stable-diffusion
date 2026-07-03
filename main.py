# ==============================================================================
# Geração de Imagens com Stable Diffusion v1.5 no Google Colab
# ==============================================================================

# 1. Instalação das bibliotecas necessárias (caso execute no ambiente local ou Colab)
# !pip install diffusers transformers torch

import time
from diffusers import StableDiffusionPipeline
import torch

# 2. Configuração do Modelo e Pipeline
# Carrega o modelo pré-treinado em precisão float16 para otimizar o uso de memória VRAM
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

# Aloca o pipeline na GPU (Aceleração por Hardware)
pipe = pipe.to("cuda")

# 3. Definição do Prompt de Entrada
prompt = "a mouse running from a cat"

print(f"Iniciando a geração para o prompt: '{prompt}'...")

# 4. Inferência e Medição de Tempo
inicio = time.time()

# Executa o modelo de difusão
image = pipe(prompt).images[0]

fim = time.time()

# 5. Salvamento e Exibição do Resultado
output_filename = "generated_image.png"
image.save(output_filename)
print(f"Imagem salva com sucesso como '{output_filename}'")

# Exibe o tempo exato de execução do pipeline
tempo_total = fim - inicio
print(f"\nTempo de geração da imagem: {tempo_total:.2f} segundos")
