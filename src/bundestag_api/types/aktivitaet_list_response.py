# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .aktivitaet import Aktivitaet
from .list_response_base import ListResponseBase

__all__ = ["AktivitaetListResponse"]


class AktivitaetListResponse(ListResponseBase):
    documents: List[Aktivitaet]
