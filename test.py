def test_answer(answer):
    """
    Teste simples para verificar se o RAG conseguiu produzir uma resposta.
    """

    if answer is None:
        return False

    if len(answer.strip()) == 0:
        return False

    return True


def test_contains_keyword(answer, keyword):
    """
    Verifica se a resposta contém uma palavra esperada.
    """

    return keyword.lower() in answer.lower()


def run_tests(rag, question, expected_keyword=None):
    """
    Executa todos os testes sobre o RAG.
    """

    answer = rag.query(question)

    results = []

    # Teste 1: resposta não vazia
    results.append(
        test_answer(answer)
    )

    # Teste 2: palavra esperada
    if expected_keyword is not None:
        results.append(
            test_contains_keyword(
                answer,
                expected_keyword
            )
        )

    # O mutante é considerado detectado
    # se algum teste falhar.
    passed = all(results)

    return {
        "passed": passed,
        "answer": answer,
        "tests": results
    }

