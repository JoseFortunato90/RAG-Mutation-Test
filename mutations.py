# M00
# teste sem mutações, tamanhos de parêmetros padrões
def M00_no_mutations(chunk_size=500,chunk_overlap=100,top_k=3):
    return {
        "chunk_size": chunk_size,
        "chunk_overlap": chunk_overlap,
        "top_k": top_k
    }

# M01
# altera o tamanho dos chunks
def M01_alter_chunk_size(chunk_size=100):
    return {
        "chunk_size": chunk_size,
        "chunk_overlap": 100,
        "top_k": 3
    }


# M02
# altera o overlap entre os chunks
def M02_alter_overlap(chunk_overlap=0):
    return {
        "chunk_size": 500,
        "chunk_overlap": chunk_overlap,
        "top_k": 3
    }


# M03
# altera a quantidade de documentos recuperados
def M03_alter_top_k(top_k=1):
    return {
        "chunk_size": 500,
        "chunk_overlap": 100,
        "top_k": top_k
    }


# M04
# Inverte a ordem dos documentos recuperados
def M04_reverse_documents(documents):
    return documents[::-1]


# M05
# Remove o documento mais relevante
def M05_remove_best_document(documents):
    return documents[1:]

