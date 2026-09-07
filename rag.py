import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


load_dotenv()


class RAG:
    def __init__(
                self,
                pdf_path,
                chunk_size=500,
                chunk_overlap=100,
                top_k=3
        ):
        self.pdf_path = pdf_path

        # LLM
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash",
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0
        )

        # Embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Parâmetros do RAG
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.top_k = top_k

        # Carrega e prepara os documentos
        self.documents = self.load_documents()

        # Cria o banco vetorial
        self.vectorstore = self.create_vectorstore()


    def load_documents(self):
        """Carrega o PDF e divide em chunks."""

        loader = PyPDFLoader(self.pdf_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

        chunks = splitter.split_documents(documents)

        print(f"Documentos carregados: {len(documents)}")
        print(f"Chunks criados: {len(chunks)}")

        return chunks


    def create_vectorstore(self):
        """Cria o banco vetorial Chroma."""

        vectorstore = Chroma.from_documents(
            documents=self.documents,
            embedding=self.embeddings,
            collection_name="rag_collection"
        )

        return vectorstore


    def retrieve(self, question):
        """Recupera os documentos mais relevantes."""

        retriever = self.vectorstore.as_retriever(
            search_kwargs={
                "k": self.top_k
            }
        )

        documents = retriever.invoke(question)

        return documents


    def generate(self, question, documents, prompt):
        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        prompt_final = prompt.format(
            context=context,
            question=question
        )

        response = self.llm.invoke(prompt_final)

        if isinstance(response.content, list):
            return "".join(
                item["text"]
                for item in response.content
                if isinstance(item, dict) and item.get("type") == "text"
            )

        return response.content


    def query(self, question, prompt):
        documents = self.retrieve(question)
        return self.generate(question, documents, prompt)