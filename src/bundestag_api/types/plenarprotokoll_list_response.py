# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .plenarprotokoll import Plenarprotokoll
from .list_response_base import ListResponseBase

__all__ = ["PlenarprotokollListResponse"]


class PlenarprotokollListResponse(ListResponseBase):
    documents: List[Plenarprotokoll]
