from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Define como uma mensagem de eero será representada
    """
    message: str
    details: str
    status: int
