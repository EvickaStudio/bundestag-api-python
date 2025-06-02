# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .drucksache_text import DrucksacheText
from .list_response_base import ListResponseBase

__all__ = ["DrucksacheTextListResponse"]


class DrucksacheTextListResponse(ListResponseBase):
    documents: List[DrucksacheText]
