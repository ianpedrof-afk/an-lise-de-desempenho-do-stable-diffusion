# Análise de Performance e Semântica: Stable Diffusion v1.5

Este repositório contém o script e o relatório técnico de uma atividade prática desenvolvida no ambiente **Google Colab**, utilizando aceleração por hardware (GPU) para explorar, avaliar e analisar o desempenho do modelo generativo **Stable Diffusion v1.5** sob diferentes estímulos textuais (*prompts*).

## 🚀 Objetivo do Projeto

O objetivo principal desta atividade foi analisar de forma quantitativa e qualitativa o comportamento do modelo de difusão latente, considerando critérios específicos como:
*   **Tempo de Inferência:** O impacto da complexidade do texto no tempo físico de processamento da GPU.
*   **Fidelidade Semântica:** A capacidade do modelo de traduzir instruções textuais em representações visuais coerentes.
*   **Qualidade Visual e Anatômica:** A identificação de artefatos visuais ou pontos de ruptura na geração de interações humanas e cenários.

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3
*   **Ambiente:** Google Colab (com backend de GPU)
*   **Frameworks/Bibliotecas:**
    *   `Hugging Face Diffusers` (Pipeline do Stable Diffusion)
    *   `Transformers`
    *   `PyTorch` (Otimizado com `torch.float16`)

## 📊 Sumário dos Resultados Obtidos

Durante a atividade, múltiplos testes foram realizados variando o escopo do prompt. A tabela abaixo consolida os padrões identificados:

| Prompt de Teste | Categoria do Prompt | Tempo de Inferência | Qualidade Anatômica / Visual | Coerência de Cenário |
| :--- | :--- | :--- | :--- | :--- |
| `a group of people dancing` | Múltiplos Humanos / Abstrato | ~8.06s | **Baixa** (Massa amorfa corporais) | Média |
| `A goalkeeper and a striker...` | Dois Humanos / Interação Rígida | ~7.92s | **Baixa** (Fusão e amálgama de corpos) | Média-Alta |
| `a beautiful woman in a cafeteria` | Humano Único / Retrato | ~7.85s | **Média-Alta** (Pequenas assimetrias nos olhos) | **Altíssima** |
| `a baseball stadium` | Cenário Macro / Sem Humanos | ~7.54s | **N/A** (Não aplicável) | **Altíssima** |

## 🧠 Principais Conclusões Técnicas

1. **Independência do Tempo de Inferência:** Os testes empíricos demonstraram que o tempo de processamento físico (flutuando estritamente entre 7,54s e 8,06s) **não é ditado pela complexidade do texto**. Ele funciona como uma constante matemática baseada no hardware utilizado e nas configurações fixas de resolução (512x512) e passos de amostragem (*sampling steps*).
2. **A Regra do Sujeito Único:** O Stable Diffusion v1.5 nativo apresenta limitações severas na divisão de tarefas lógicas para gerar múltiplos personagens interagindo. No entanto, exibe um desempenho excepcional e fotorrealista ao focar em um único sujeito (retratos) ou em estruturas inanimadas/cenários macro de grande escala.

## 📋 Como Executar o Código

1. Abra um novo notebook no [Google Colab](https://colab.research.google.com/).
2. Certifique-se de ativar a aceleração por GPU em: *Ambiente de Execução > Alterar tipo de ambiente de execução > Acelerador de hardware (T4 GPU)*.
3. Instale as dependências executando:
   ```bash
   pip install diffusers transformers torch
