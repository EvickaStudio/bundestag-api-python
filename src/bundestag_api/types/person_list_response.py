# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .person import Person
from .list_response_base import ListResponseBase

__all__ = ["PersonListResponse"]


class PersonListResponse(ListResponseBase):
    documents: List[Person]
