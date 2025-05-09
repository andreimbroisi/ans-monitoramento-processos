# Requisitos de Negócio - Projeto de Automação dos ANS

## Objetivo

Automatizar a coleta, validação, exportação e visualização dos dados de Acordos de Nível de Serviço (ANS), garantindo maior agilidade, confiabilidade e padronização na análise mensal dos indicadores por superintendência.

---

## Regras de Negócio

1. **Periodicidade**
   - A coleta e análise dos indicadores deve ser realizada **mensalmente**.
   - Os dados devem ser enviados pelas superintendências até o **5º dia útil de cada mês**.

2. **Coleta de Dados**
   - Os dados serão fornecidos em **planilhas Excel** com estrutura padronizada.
   - O processo de leitura será automatizado via script Python.

3. **Validação**
   - Todos os campos obrigatórios devem ser preenchidos.
   - Valores nulos ou fora dos padrões acordados devem gerar **alerta automático** por e-mail.

4. **Alertas**
   - Indicadores fora do ANS (Acordo de Nível de Serviço) disparam **notificações automáticas**.
   - O e-mail de notificação segue um template definido com nome do indicador, superintendência e prazo para resposta.

5. **Exportação**
   - Após validação, os dados devem ser exportados em formatos `.json` ou `.txt` para uso no Power BI ou outros sistemas.

6. **Visualização**
   - Um painel em Power BI consolidará os dados, permitindo análise por mês e por superintendência.
   - KPIs destacados devem incluir:
     - Indicadores dentro e fora do padrão
     - Superintendências com maior índice de não conformidade
     - Tendências de melhoria ou piora

---

## Requisitos Funcionais Relacionados

- Leitura automatizada de arquivos Excel.
- Tratamento de valores nulos e inconsistentes.
- Exportação em formato compatível com BI.
- Integração com fluxo Bizagi para aprovação/validação.
- Gatilho de notificação via e-mail.
