import pandas as pd
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. Carregar o JSON
with open("automacao/relatorio_ans.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# 2. Converter para DataFrame
df = pd.DataFrame(dados)

# 3. Criar coluna de status
df["Status"] = df.apply(lambda row: "Conforme" if row["Resultado"] >= row["Meta"] else "Não Conforme", axis=1)

# 4. Filtrar os indicadores fora do padrão
nao_conformes = df[df["Status"] == "Não Conforme"]

# 5. Configuração de e-mail
remetente = "seuemail@gmail.com"
senha = "sua_senha_de_app"  # Use senha de app se for Gmail
destinatarios = ["destinatario1@email.com", "destinatario2@email.com"]

# 6. Enviar e-mails
for _, linha in nao_conformes.iterrows():
    assunto = "Alerta de não conformidade - Indicador fora do ANS"
    corpo = f"""
    Prezado(a),

    Identificamos que o indicador **{linha['Indicador']}** da superintendência **{linha['Superintendência']}**
    encontra-se fora dos parâmetros estabelecidos.

    Resultado atual: {linha['Resultado']} | Meta: {linha['Meta']}

    Favor providenciar análise até o 5º dia útil do mês.

    Att,
    Equipe de Qualidade
    """

    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = ", ".join(destinatarios)
    msg["Subject"] = assunto
    msg.attach(MIMEText(corpo, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(remetente, senha)
        server.sendmail(remetente, destinatarios, msg.as_string())

print("E-mails de alerta enviados com sucesso.")
