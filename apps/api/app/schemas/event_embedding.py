from pydantic import BaseModel, ConfigDict


class EventEmbeddingRead(BaseModel):
    id: str
    event_id: str
    vector_provider: str
    embedding_model: str
    embedding_dimension: int
    storage_reference: str
    model_config = ConfigDict(from_attributes=True)

