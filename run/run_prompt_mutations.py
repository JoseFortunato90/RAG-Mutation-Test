import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from rag import RAG

from mutations.mutations_prompt import (
    M00_no_mutations,
    M01_prompt_mutations,
    M02_prompt_mutations,
    M03_prompt_mutations,
    M04_prompt_mutations,
    M05_prompt_mutations
)

PDF_PATH = "data/document.pdf"
QUESTION = "O que é heap sort?"

def run_mutation(name, rag, config):

    print("\n" + "=" * 50)
    print(f"Mutante: {name}")
    print("=" * 50)

    PROMPT = config['prompt']

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

    rag = RAG(
            PDF_PATH,
            chunk_size=500,
            chunk_overlap=100,
            top_k=3
        )

    mutations = {
    "M00 - no mutations": M00_no_mutations(),
    "M01 - remove contexto": M01_prompt_mutations(),
    "M02 - remove instrução": M02_prompt_mutations(),
    "M03 - erros de escrita": M03_prompt_mutations(),
    "M04 - ação incorreta": M04_prompt_mutations(),
    "M05 - sem prompt": M05_prompt_mutations()
    }

    killed = 0
    total = len(mutations)

    for name, config in mutations.items():

        passed = run_mutation(
            name,
            rag,
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