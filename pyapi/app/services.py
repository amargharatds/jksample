import openai
import numpy as np

openai.api_key = "your_openai_api_key"

async def generate_embedding(text: str) -> list:
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

async def retrieve_answer(question: str, embeddings: list, texts: list) -> str:
    question_embedding = await generate_embedding(question)
    similarities = [np.dot(question_embedding, emb) for emb in embeddings]
    most_relevant_idx = np.argmax(similarities)
    return texts[most_relevant_idx]
