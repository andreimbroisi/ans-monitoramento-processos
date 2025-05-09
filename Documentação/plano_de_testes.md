# Plano de Testes

## Objetivo
Garantir que o sistema funcione corretamente em todos os cenários críticos.

## Casos de Teste

### Teste 1: Importação válida
- **Entrada**: Planilha `ans_2024.xlsx` com todos os campos preenchidos.
- **Resultado esperado**: Geração do arquivo `relatorio_ans.json` sem erros.

### Teste 2: Dados ausentes
- **Entrada**: Planilha com campos nulos.
- **Resultado esperado**: Substituição por "N/A" ou 0; aviso no console.

### Teste 3: Indicadores fora do padrão
- **Entrada**: Planilha com valores fora do ANS.
- **Resultado esperado**: Geração de e-mail de alerta com informações da violação.

### Teste 4: Execução automática
- **Entrada**: Script agendado no Windows.
- **Resultado esperado**: Execução automática conforme o horário definido.

## Ferramentas
- Prompt de comando (CMD)
- Python 3.12
- Power BI para validação visual