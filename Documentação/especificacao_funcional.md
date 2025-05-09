
# 📄 Especificação Funcional  
**Projeto:** Monitoramento Automatizado de Indicadores de ANS  
**Data:** 09/05/2025  
**Versão:** 1.0  
**Autor:** André Imbroisi - imbroisi@gmail.com

## 1. Objetivo do Projeto

Este projeto tem como objetivo automatizar a coleta, tratamento, validação e visualização de indicadores relacionados aos **Acordos de Nível de Serviço (ANS)** das superintendências de uma organização, com foco em garantir conformidade com os parâmetros estabelecidos, facilitar o monitoramento de metas e viabilizar a tomada de decisão com base em dados atualizados.

## 2. Público-Alvo

- Gestores de Qualidade  
- Analistas de Performance  
- Coordenadores de Superintendências  
- Diretores de Área  

## 3. Funcionalidades Principais

| Funcionalidade                       | Descrição                                                                 |
|-------------------------------------|---------------------------------------------------------------------------|
| **Importação de dados Excel**       | Leitura automática de uma planilha com os indicadores mensais.           |
| **Tratamento de dados**             | Substituição de valores nulos, formatação e validação dos campos.        |
| **Exportação para JSON**            | Geração de arquivo `.json` com os dados tratados para integração.        |
| **Integração com Bizagi**           | O JSON alimenta um fluxo de processo para avaliação e providências.      |
| **Dashboard Power BI**              | Painel interativo com os principais KPIs dos ANS para visualização.      |
| **Agendamento automático**          | Execução automatizada do script em datas definidas via agendador do SO.  |
| **Alertas (futuro)**                | Gatilhos para envio de e-mails ou notificações se indicador estiver fora do padrão. *(opcional)*

## 4. Regras de Negócio

- Todos os indicadores devem ser atualizados **mensalmente até o 5º dia útil**.
- Indicadores com valores nulos devem ser preenchidos com `"N/A"` ou `0`, dependendo do tipo (texto ou número).
- Indicadores fora da meta definida devem ser sinalizados no fluxo do Bizagi.
- Os dados exportados para JSON devem manter o nome exato das colunas utilizadas no Excel.

## 5. Entradas Esperadas

- Planilha `ans_2024.xlsx` contendo:
  - Nome da superintendência
  - Indicador
  - Valor obtido
  - Meta esperada
  - Data de referência
  - Observações

## 6. Saídas Esperadas

- Arquivo `relatorio_ans.json` contendo os dados estruturados e limpos.
- Atualização do painel Power BI com os dados do JSON.
- Execução do fluxo no Bizagi com base nas informações importadas.
- (Futuro) Alerta automático para responsáveis por superintendência fora do padrão.

## 7. Frequência de Atualização

- **Mensal**, com execução automática ou manual do script `coletor_ans.py`.

## 8. Integrações

| Sistema | Tipo de Integração | Direção | Observação |
|--------|---------------------|---------|------------|
| Power BI | JSON como fonte de dados | Entrada | Conecta ao `relatorio_ans.json` |
| Bizagi | Abertura de tarefa por API ou manual | Entrada | Usuário analisa indicadores fora da meta |
| Python | Script de automação | Local | Processamento local agendado |

## 9. Restrições

- O script Python deve rodar em ambiente com permissões de leitura/escrita local.
- O Power BI só atualiza dados localmente ou via gateway, conforme configuração.
- O Bizagi deve estar acessível (instância web ou desktop).
- O nome e a estrutura das colunas da planilha não podem ser alterados sem atualização no script.

## 10. Futuras Melhorias

- Integração direta com bancos de dados corporativos (SQL Server, Oracle).
- Geração de alertas automáticos por e-mail usando SMTP.
- Criação de log de execução e histórico de conformidades.
