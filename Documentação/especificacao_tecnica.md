# Especificação Técnica

## Linguagem
- Python 3.13

## Bibliotecas
- pandas
- openpyxl
- json
- pathlib

## Estrutura de Diretórios
```
/Automacao
  ├── coletor_ans.py
  └── relatorio_ans.json
/exemplos_dados
  └── ans_2024.xlsx
/documentos
  ├── especificacao_funcional.md
  ├── especificacao_tecnica.md
  ├── plano_de_testes.md
  └── requisitos_de_negocio.md
```

## Requisitos de Software
- Python 3.12
- Power BI Desktop
- Bizagi Modeler
- Windows com Agendador de Tarefas

## Comandos principais
```bash
python Automacao/coletor_ans.py
```

## Integrações
- Power BI: Leitura direta do arquivo `relatorio_ans.json`
- Bizagi: Chamada de script Python como tarefa externa