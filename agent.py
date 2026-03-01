class OrionSalesAgent:
    def __init__(self, name):
        self.name = name

    def generate_strategy(self, business, audience, goal):
        return f"""
Você é {self.name}, um estrategista de vendas e marketing de elite.

NEGÓCIO:
{business}

PÚBLICO:
{audience}

OBJETIVO:
{goal}

Tarefas:
1. Diagnosticar o principal gargalo de vendas
2. Criar uma proposta clara e direta
3. Gerar um script de abordagem para Instagram ou WhatsApp
4. Criar uma copy curta e persuasiva
5. Sugerir próximo passo comercial

Responda de forma prática, direta e aplicável.
"""
