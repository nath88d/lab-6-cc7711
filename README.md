# Extração de Contornos com OpenCV

## Imagens Utilizadas
![image](https://github.com/user-attachments/assets/9baf3609-5704-414a-aeeb-c7f26f562a62)
![image](https://github.com/user-attachments/assets/dc42f129-ba48-4cd8-ba35-81e7ac27de40)

![image](https://github.com/user-attachments/assets/d4f1ec1c-2d77-4ed0-bf27-202160fc5f81)

---

## Etapas do Processamento da Imagem

As imagens passam por um conjunto de etapas básicas para facilitar a detecção de seus contornos. Veja abaixo o que acontece em cada fase:
* Leitura e Conversão
- A imagem é carregada e convertida para o formato de cores correto (RGB).
- Depois, ela é transformada em preto e branco (escala de cinza) para facilitar o tratamento.

* Binarização
- A imagem em tons de cinza é convertida para **preto e branco puro**.
- O valor que define o que será preto ou branco (limiar) pode ser fixo ou calculado a partir do brilho da imagem.

* Aplicação de Filtros (Kernel)
- Um **pequeno bloco de pixels (kernel)** é criado para aplicar operações que melhoram a qualidade da imagem.
- Esse bloco ajuda a corrigir falhas e remover ruídos.

* Operações Morfológicas (opcional)
- Se necessário, são aplicadas etapas que:
  - Preenchem espaços vazios nos objetos.
  - Conectam partes separadas.
  - Eliminam pequenos ruídos isolados.

* Suavização (Blur)
- A imagem é levemente borrada para reduzir detalhes muito pequenos que atrapalham a detecção de bordas.

* Detecção de Bordas
- Usamos o **algoritmo de Canny**, que destaca as bordas dos objetos com base nas mudanças bruscas de cor na imagem.

* Identificação dos Contornos
- As bordas são transformadas em **contornos fechados**.
- Pode-se escolher extrair todos os contornos ou apenas os principais.
- Também é possível ignorar contornos muito pequenos ou muito grandes.

* Visualização Final
- Os contornos são desenhados em cima da imagem original.
- As diferentes etapas são mostradas lado a lado para facilitar a análise do processo.

---

##  Parâmetros Utilizados e resultados

###  Girafa
- `limiar`: valor fixo `10`
- `kernel`: 5x5
- `morfologia`: desativado
- `canny`: `threshold1 = 0.5 * brilho`, `threshold2 = 0.5 * brilho`
- `área mínima/máxima`: não definido
![image](https://github.com/user-attachments/assets/7684e824-b0c4-4354-a497-5bd12695d6cb)

###  Avião
- `limiar`: `0.35 * brilho máximo`
- `kernel`: 5x5
- `morfologia`: ativado
- `canny`: `threshold1 = 0.55 * brilho`, `threshold2 = 0.55 * brilho`
- `área mínima`: 4000
- `área máxima`: 120000
![image](https://github.com/user-attachments/assets/f5577956-4ab1-4de8-9b2c-d0f55082faf0)

###  Satélite
- `limiar`: `lambda brilho: (brilho * 35) * 0.4`
- `kernel`: 5x5
- `morfologia`: desativado
- `canny`: `threshold1 = 0.45 * brilho`, `threshold2 = 0.45 * brilho`
- `área mínima`: 800
- `área máxima`: 25000
![image](https://github.com/user-attachments/assets/d63aa398-e188-4bd7-ac89-1b3ad1238735)

---
