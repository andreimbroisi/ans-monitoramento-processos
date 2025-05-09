from pathlib import Path

# Conteúdo do arquivo notificacoes_email.md
conteudo_md = """
# 📬 Notificações por E-mail - Projeto de Automação dos ANS

## Objetivo

Este documento descreve o formato, a lógica e as condições para o envio automático de notificações por e-mail quando um ou mais indicadores estiverem fora dos parâmetros definidos nos Acordos de Nível de Serviço (ANS).

---

## 📌 Regras de Envio

1. **Disparo Automático**
   - A notificação deve ser enviada automaticamente ao detectar um valor fora do padrão durante a execução do script de validação.

2. **Destinatários**
   - Cada superintendência possui um e-mail responsável (pré-configurado em uma tabela ou dicionário de e-mails).
   - A Equipe de Qualidade deve ser incluída em cópia oculta (BCC) para controle.

3. **Frequência**
   - O script de validação e envio roda mensalmente via agendador de tarefas.
   - Um e-mail por indicador não conforme.

---

## 📧 Modelo de E-mail

### Assunto:

### Corpo:
Prezado(a) [Nome do Responsável],

Identificamos que o indicador [Nome do Indicador] da superintendência [Nome da Superintendência] encontra-se fora dos parâmetros estabelecidos para o mês de [Mês/Ano].

Valor informado: [Valor]
Meta esperada: [Meta]
Data de referência: [Data]

Solicitamos que a análise da não conformidade seja providenciada até [Prazo de Resposta].

Atenciosamente,
Equipe de Qualidade
[Email da Equipe de Qualidade]


---

## ⚙️ Configuração Técnica

- A biblioteca utilizada é `smtplib` com `email.message`.
- As credenciais de envio são armazenadas em um arquivo `.env` ou variáveis de ambiente.
- O servidor de e-mail deve aceitar conexões TLS/SSL.

---

## 🛠️ Trechos de Código Exemplo

```python
from email.message import EmailMessage
import smtplib

def enviar_alerta_email(destinatario, indicador, superintendencia, valor, meta, prazo):
    msg = EmailMessage()
    msg['Subject'] = '🔔 Alerta de não conformidade - Indicador fora do ANS'
    msg['From'] = 'qualidade@empresa.com'
    msg['To'] = destinatario
    msg.set_content(
        f\"\"\"Prezado(a),\\n\\n
        Identificamos que o indicador '{indicador}' da superintendência '{superintendencia}' está fora dos parâmetros.\\n
        Valor informado: {valor}\\nMeta esperada: {meta}\\n\\n
        Favor providenciar análise até {prazo}.\\n\\n
        Att, Equipe de Qualidade\"\"\"
    )

    with smtplib.SMTP_SSL('smtp.seudominio.com', 465) as smtp:
        smtp.login('qualidade@empresa.com', 'SENHA_SEGURA')
        smtp.send_message(msg)
✅ Checklist de Validação
 Indicador está fora do parâmetro

 E-mail do responsável está disponível

 Mensagem foi formatada corretamente

 Registro de envio armazenado em log
"""

Caminho para salvar o arquivo
caminho_arquivo = Path("/mnt/data/notificacoes_email.md")
caminho_arquivo.write_text(conteudo_md, encoding="utf-8")

caminho_arquivo

Resultado
PosixPath('/mnt/data/notificacoes_email.md')