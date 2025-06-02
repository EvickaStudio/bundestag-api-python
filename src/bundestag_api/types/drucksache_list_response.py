# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .drucksache import Drucksache
from .list_response_base import ListResponseBase

__all__ = ["DrucksacheListResponse"]


class DrucksacheListResponse(ListResponseBase):
    documents: List[Drucksache]
