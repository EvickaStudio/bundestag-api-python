# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Urheber"]


class Urheber(BaseModel):
    bezeichnung: str

    titel: str

    einbringer: Optional[bool] = None

    rolle: Optional[Literal["B", "U"]] = None
