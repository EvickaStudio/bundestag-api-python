# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .vorgangsposition import Vorgangsposition
from .list_response_base import ListResponseBase

__all__ = ["VorgangspositionListResponse"]


class VorgangspositionListResponse(ListResponseBase):
    documents: List[Vorgangsposition]
