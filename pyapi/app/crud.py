from app.database import get_db

async def insert_embedding(db, document_id, embedding, content):
    query = """
    INSERT INTO document_embeddings (document_id, embedding, content)
    VALUES ($1, $2, $3)
    RETURNING id;
    """
    return await db.fetchval(query, document_id, embedding, content)

async def fetch_relevant_embeddings(db, document_ids):
    query = """
    SELECT embedding, content FROM document_embeddings
    WHERE document_id = ANY($1::uuid[]);
    """
    return await db.fetch(query, document_ids)
