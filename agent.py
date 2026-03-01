import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gestor_trafego_agent(nicho, objetivo, orcamento):
    prompt = f"""
    Você é um gestor de tráfego pago sênior.
    Analise o negócio abaixo e gere um plano de ação.

    Nicho: {nicho}
    Objetivo: {objetivo}
    Orçamento mensal: {orcamento}

    Entregue:
    1. Diagnóstico do negócio
    2. Estratégia de tráfego recomendada
    3. Estrutura de campanha (Meta ou Google)
    4. Sugestão de oferta
    5. Próximo passo prático
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Você é um especialista em marketing digital e tráfego pago."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("🚀 Orion Agent - Gestor de Tráfego IA")
    nicho = input("Nicho do negócio: ")
    objetivo = input("Objetivo principal: ")
    orcamento = input("Orçamento mensal (R$): ")

    resultado = gestor_trafego_agent(nicho, objetivo, orcamento)
    print("\n📊 PLANO GERADO:\n")
    print(resultado)
