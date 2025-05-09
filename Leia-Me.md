```markdown
# 📊 Monitoramento Automatizado dos ANS

Este projeto tem como objetivo automatizar a coleta, validação e visualização dos dados de Acordos de Níveis de Serviço (ANS) utilizando Python, Power BI e agendamento no Windows.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.12
- Pandas
- Power BI Desktop
- Windows Task Scheduler
- Bizagi Modeler (para mapeamento de processos)

---

## 📁 Estrutura do Projeto

```

ans-monitoramento-processos/
│
├── Automacao/
│   ├── coletor\_ans.py                # Script principal de coleta e exportação
│   └── relatorio\_ans.json            # Arquivo gerado automaticamente
│
├── dados\_exemplo/
│   └── ans\_2024.xlsx                 # Planilha modelo dos indicadores ANS
│
├── dashboard/
│   └── painel\_ans.pbix               # Dashboard Power BI com visualizações
│
└── README.md                         # Este arquivo

````

---

## 🚀 Etapas de Execução

### 1. Atualize os Dados

Substitua o arquivo `ans_2024.xlsx` em `dados_exemplo/` com os dados atualizados da superintendência.

---

### 2. Execute o Script

```bash
python Automacao/coletor_ans.py
````

O script irá:

* Carregar a planilha
* Validar dados e preencher nulos
* Exportar os dados para `relatorio_ans.json`

---

### 3. Visualize no Power BI

Abra o arquivo `dashboard/painel_ans.pbix` no Power BI Desktop.

1. Vá em **"Página Inicial" → "Transformar Dados"**
2. Clique em **"Atualizar Pré-visualização"**
3. Clique em **"Converter em Tabela"** e depois em **"Expandir Colunas"**
4. Por fim, **"Fechar & Aplicar"** para atualizar os KPIs

---

### 4. Automatize com Agendador de Tarefas

Para automatizar a execução diária do script:

1. Abra o **Agendador de Tarefas do Windows**
2. Crie uma nova tarefa com gatilho diário ou mensal
3. Ação: `"Iniciar um programa"`
4. Caminho:

   ```
   C:\Users\SEU_USUARIO\AppData\Local\Programs\Python\Python312\python.exe
   ```

   Argumento:

   ```
   "C:\caminho\completo\para\Automacao\coletor_ans.py"
   ```

---

## 📬 Alerta por E-mail (Opcional)

Você pode integrar o script com envio de alertas por e-mail usando `smtplib` para notificar responsáveis caso indicadores estejam fora dos padrões.

---

## 🧩 Fluxo de Processo (Bizagi)

O processo foi mapeado no Bizagi Modeler com as seguintes etapas:

* Recebimento de dados das superintendências
* Validação e processamento com script Python
* Geração de relatórios e alertas
* Visualização no painel Power BI

---

## ✅ Checklist Final

* [x] Planilha ANS atualizada
* [x] Script Python funcionando
* [x] JSON exportado corretamente
* [x] Painel Power BI vinculado ao JSON
* [x] Tarefa agendada
* [x] Documentação publicada


## 👤 Autor

André Imbroisi 
Analista de Processos | Automação de Dados
\[imbroisi@gmail.com]

