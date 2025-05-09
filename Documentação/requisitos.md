# Requisitos Funcionais e Não Funcionais - Projeto de Automação dos ANS

## 🧩 Requisitos Funcionais

1. **Coleta de Dados**
   - O sistema deve ler automaticamente arquivos `.xlsx` com dados de indicadores dos ANS.
   - O script deve localizar os arquivos em pastas organizadas por mês e superintendência.

2. **Validação de Dados**
   - O sistema deve identificar e tratar campos obrigatórios vazios (valores nulos).
   - Deve validar se os indicadores estão dentro dos parâmetros acordados.
   - Caso um valor esteja fora do padrão, o sistema deve marcar e registrar essa ocorrência.

3. **Geração de Alerta**
   - Quando um indicador estiver fora dos padrões, deve ser gerado um e-mail automático para a superintendência responsável.
   - O alerta deve conter: nome do indicador, superintendência, valor registrado e prazo para resposta.

4. **Exportação de Dados**
   - Os dados validados devem ser exportados para um arquivo `.json` e/ou `.txt` com estrutura legível e padronizada.
   - Os arquivos exportados devem estar disponíveis em um diretório de saída para integração com o Power BI.

5. **Painel em Power BI**
   - O sistema deve permitir que o Power BI consuma os dados `.json` para geração de gráficos e indicadores.
   - O painel deve apresentar: indicadores mensais, status (conforme/não conforme), e filtros por superintendência e data.

6. **Agendamento do Script**
   - O script de coleta e validação deve ser executado automaticamente via Agendador de Tarefas (Windows Scheduler) em um intervalo mensal.

7. **Fluxo no Bizagi**
   - O processo de coleta e validação de dados deve ser representado visualmente no Bizagi.
   - O Bizagi deve conter tarefas para: entrada de dados, validação, alerta e aprovação de conformidade.

---

## 🛡️ Requisitos Não Funcionais

1. **Compatibilidade**
   - O sistema deve ser compatível com Windows 10 ou superior.
   - O script deve ser escrito em Python 3.12 ou superior.

2. **Desempenho**
   - A execução do script não deve exceder 60 segundos para planilhas com até 1.000 linhas.

3. **Confiabilidade**
   - Todos os dados exportados devem ser validados antes de serem disponibilizados para análise.
   - Logs de erro devem ser gerados automaticamente em caso de falhas.

4. **Segurança**
   - Os dados sensíveis devem ser armazenados de forma segura e com acesso restrito.
   - As notificações devem ser enviadas apenas para usuários autorizados.

5. **Manutenibilidade**
   - O código deve estar versionado no GitHub.
   - O repositório deve conter documentação clara (`README.md`, `requisitos_funcionais.md`, `especificacao_funcional.md`).

6. **Escalabilidade**
   - A estrutura deve permitir a adição de novas superintendências ou indicadores sem necessidade de reescrita do código-fonte.


