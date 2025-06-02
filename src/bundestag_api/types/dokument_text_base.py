# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DokumentTextBase"]


class DokumentTextBase(BaseModel):
    text: Optional[str] = None
    """Volltext des Dokuments

    Das Beispiel enthält einen gekürzten Auszug einer Drucksache.
    """
