# Vitrine · Favoritos Renner

Página pública com os looks que Nicole Dagostim escolheu na Renner. Cada peça tem foto e um botão **Comprar** que vai direto para o link de afiliada (Awin).

Endereço previsto: https://nicoledagostim.github.io/vitrine/ (botão "Favoritos Renner" na seção Vitrines do Linktree).

## Como funciona

1. **Notion é o cadastro.** Banco "Favoritos Renner · Links de afiliada". Cada look tem foto, link de afiliada, categoria, status.
2. **Link de afiliada sempre gerado no Link Builder da Awin**, com o login da Nicole (publisher 2599889, anunciante 70694), com `clickref` identificando a peça. Nunca montado à mão.
3. **`looks.json`** guarda os looks que aparecem na vitrine (nome, cor, categoria, foto, link, em promoção).
4. **`build.py`** lê `looks.json` e gera o `index.html` (página estática, pensada para celular).
5. Para atualizar: pedir "atualiza a vitrine". Os looks marcados para a vitrine no Notion entram em `looks.json`, roda-se `python3 build.py` e faz-se commit.

## Notas

- A página tem aviso de links de afiliada (boa prática de divulgação).
- Fotos: são as fotos de produto da Renner (`img.lojasrenner.com.br`), referenciadas em `looks.json`. Se alguma sumir, trocar pelo endereço novo da foto no site da Renner.
- Comissão só existe quando a compra é aprovada pela Renner. Clique no relatório da Awin prova rastreamento, não comissão.

## Decisões de construção

- Notion como cadastro; página estática gerada por `build.py` a partir de `looks.json`.
- Hospedagem no GitHub Pages (grátis, repositório público); botão "Favoritos Renner 🛍️" na seção Vitrines do Linktree.
- Layout: grade compacta de miniaturas, 2 colunas no celular (4 em tela grande), botão "Comprar" em cada peça.
- Fotos: usa as fotos de produto da Renner, sem fotos pessoais no repositório.
- Links sempre gerados no Link Builder da Awin, com o login da Nicole.
