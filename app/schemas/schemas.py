from pydantic import BaseModel


class ImageUrl(BaseModel):
    url: str
    name: str | None = None
