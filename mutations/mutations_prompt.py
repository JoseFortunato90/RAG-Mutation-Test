from langchain_core.prompts import ChatPromptTemplate


# M00
# Teste sem mutação
def M00_no_mutations():
    return {
        "prompt": ChatPromptTemplate.from_template("""
            Você é um assistente que responde perguntas
            utilizando somente as informações presentes no contexto.

            Se a resposta não estiver no contexto,
            diga que não foi possível encontrar a informação.

            Contexto:
            {context}

            Pergunta:
            {question}

            Resposta:
        """)
    }


# M01
# Responde independente do contexto
def M01_prompt_mutations():
    return {
        "prompt": ChatPromptTemplate.from_template("""
            Você é um assistente que responde perguntas
            independente do contexto dado, o importante é dar uma resposta.

            Contexto:
            {context}

            Pergunta:
            {question}

            Resposta:
        """)
    }


# M02
# Remove a contextualização da ação da LLM
def M02_prompt_mutations():
    return {
        "prompt": ChatPromptTemplate.from_template("""
            Se a resposta não estiver no contexto,
            diga que não foi possível encontrar a informação.

            Contexto:
            {context}

            Pergunta:
            {question}

            Resposta:
        """)
    }


# M03
# Prompt com erros de escrita e abreviações
def M03_prompt_mutations():
    return {
        "prompt": ChatPromptTemplate.from_template("""
            Vc e um assitente q resp pergunta
            usano somente as info presentes no contesto.

            Si a resp n tiver no contesto,
            diga que n foi possevel encontra a informacao.

            Contexto:
            {context}

            Pergunta:
            {question}

            Resposta:
        """)
    }