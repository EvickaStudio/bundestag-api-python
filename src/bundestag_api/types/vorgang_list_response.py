# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .vorgang import Vorgang
from .list_response_base import ListResponseBase

__all__ = ["VorgangListResponse"]


class VorgangListResponse(ListResponseBase):
    documents: List[Vorgang]
