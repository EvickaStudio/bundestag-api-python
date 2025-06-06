# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ListResponseBase"]


class ListResponseBase(BaseModel):
    cursor: str

    num_found: int = FieldInfo(alias="numFound")
