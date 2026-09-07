import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from rag import RAG
from langchain_core.prompts import ChatPromptTemplate

from mutations.mutations_rag import (
    M01_alter_chunk_size,
    M02_alter_overlap,
    M03_alter_top_k,
    M00_no_mutations
)


PDF_PATH = "data/document.pdf"

QUESTION = "O que é quick sort"
EXPECTED_KEYWORD = None

PROMPT = ChatPromptTemplate.from_template("""
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


def run_mutation(name, config):

    print("\n" + "=" * 50)
    print(f"Mutante: {name}")
    print("=" * 50)

    rag = RAG(
        PDF_PATH,
        chunk_size=config["chunk_size"],
        chunk_overlap=config["chunk_overlap"],
        top_k=config["top_k"]
    )

    answer = rag.query(QUESTION, PROMPT)

    print("\nResposta:")
    print(answer)

    # Teste
    if answer is not None and len(answer.strip()) > 0:

        print("\nResultado: PASSOU")

        return True

    else:

        print("\nResultado: FALHOU")

        return False


def main():

    mutations = {
        "M0 - no mutations": M00_no_mutations(),
        "M01 - alter Chunk Size": M01_alter_chunk_size(),
        "M02 - alter Overlap": M02_alter_overlap(),
        "M03 - alter Top K": M03_alter_top_k()
    }

    killed = 0
    total = len(mutations)

    for name, config in mutations.items():

        passed = run_mutation(
            name,
            config
        )

        if not passed:
            killed += 1

    mutation_score = (killed / total) * 100

    print("\n" + "=" * 50)
    print("RESULTADO FINAL")
    print("=" * 50)

    print(f"Total de mutações: {total}")
    print(f"Mutações detectadas: {killed}")
    print(f"Mutações sobreviventes: {total - killed}")
    print(f"Mutation Score: {mutation_score:.2f}%")


if __name__ == "__main__":
    main()

