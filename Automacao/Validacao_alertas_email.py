# Limites dos indicadores
limites = {
    "Respostas em até 5 dias (%)": 90,
    "Satisfação do Usuário (%)": 80
}

# Validação e coleta de não conformidades
nao_conformes = []
for linha in dados_dict:
    for indicador, limite in limites.items():
        if indicador in linha and isinstance(linha[indicador], (int, float)):
            if linha[indicador] < limite:
                nao_conformes.append({
                    "superintendência": linha.get("Superintendência", "N/A"),
                    "indicador": indicador,
                    "valor": linha[indicador]
                })

# Exibir alertas no console (ou por e-mail)
if nao_conformes:
    print("🔴 Indicadores fora do padrão detectados:")
    for item in nao_conformes:
        print(f"- {item['indicador']} da {item['superintendência']} está em {item['valor']}%")

    # Aqui você pode acionar o envio de e-mail se quiser
else:
    print("✅ Todos os indicadores estão dentro dos padrões.")
