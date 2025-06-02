# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .list_response_base import ListResponseBase
from .plenarprotokoll_text import PlenarprotokollText

__all__ = ["PlenarprotokollTextListResponse"]


class PlenarprotokollTextListResponse(ListResponseBase):
    documents: List[PlenarprotokollText]
