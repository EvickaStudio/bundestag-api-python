# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Vorgangsbezug"]


class Vorgangsbezug(BaseModel):
    id: str
    """ID eines verknüpften Vorgangs"""

    titel: str

    vorgangstyp: str
