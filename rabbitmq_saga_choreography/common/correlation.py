import uuid


def create_saga_id() -> str:
    """
    Generate a unique Saga/Correlation ID.
    """
    return str(uuid.uuid4())