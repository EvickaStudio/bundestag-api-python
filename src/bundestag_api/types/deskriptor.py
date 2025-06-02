# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Deskriptor"]


class Deskriptor(BaseModel):
    name: str

    typ: Literal[
        "Freier Deskriptor", "Geograph. Begriffe", "Institutionen", "Personen", "Rechtsmaterialien", "Sachbegriffe"
    ]
