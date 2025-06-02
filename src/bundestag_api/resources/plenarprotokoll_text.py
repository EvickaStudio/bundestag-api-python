# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import plenarprotokoll_text_list_params, plenarprotokoll_text_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.plenarprotokoll_text import PlenarprotokollText
from ..types.plenarprotokoll_text_list_response import PlenarprotokollTextListResponse

__all__ = ["PlenarprotokollTextResource", "AsyncPlenarprotokollTextResource"]


class PlenarprotokollTextResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlenarprotokollTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bundestag-api-python#accessing-raw-response-data-eg-headers
        """
        return PlenarprotokollTextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlenarprotokollTextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bundestag-api-python#with_streaming_response
        """
        return PlenarprotokollTextResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: int,
        *,
        format: Literal["json", "xml"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlenarprotokollText:
        """
        Liefert Volltext und Metadaten zu einem Plenarprotokoll

        Args:
          format: Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder
              XML.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/plenarprotokoll-text/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"format": format}, plenarprotokoll_text_retrieve_params.PlenarprotokollTextRetrieveParams
                ),
            ),
            cast_to=PlenarprotokollText,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        f: plenarprotokoll_text_list_params.F | NotGiven = NOT_GIVEN,
        format: Literal["json", "xml"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlenarprotokollTextListResponse:
        """
        Liefert eine Liste von Volltexten und Metadaten zu Plenarprotokollen

        Args:
          cursor: Position des Cursors zur Anfrage weiterer Entitäten

              Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine
              Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage
              wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden
              und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es
              können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr
              ändert. Dies signalisiert, dass alle Entitäten geladen wurden.

          format: Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder
              XML.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/plenarprotokoll-text",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "f": f,
                        "format": format,
                    },
                    plenarprotokoll_text_list_params.PlenarprotokollTextListParams,
                ),
            ),
            cast_to=PlenarprotokollTextListResponse,
        )


class AsyncPlenarprotokollTextResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlenarprotokollTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bundestag-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlenarprotokollTextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlenarprotokollTextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bundestag-api-python#with_streaming_response
        """
        return AsyncPlenarprotokollTextResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: int,
        *,
        format: Literal["json", "xml"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlenarprotokollText:
        """
        Liefert Volltext und Metadaten zu einem Plenarprotokoll

        Args:
          format: Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder
              XML.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/plenarprotokoll-text/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"format": format}, plenarprotokoll_text_retrieve_params.PlenarprotokollTextRetrieveParams
                ),
            ),
            cast_to=PlenarprotokollText,
        )

    async def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        f: plenarprotokoll_text_list_params.F | NotGiven = NOT_GIVEN,
        format: Literal["json", "xml"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlenarprotokollTextListResponse:
        """
        Liefert eine Liste von Volltexten und Metadaten zu Plenarprotokollen

        Args:
          cursor: Position des Cursors zur Anfrage weiterer Entitäten

              Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine
              Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage
              wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden
              und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es
              können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr
              ändert. Dies signalisiert, dass alle Entitäten geladen wurden.

          format: Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder
              XML.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/plenarprotokoll-text",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "f": f,
                        "format": format,
                    },
                    plenarprotokoll_text_list_params.PlenarprotokollTextListParams,
                ),
            ),
            cast_to=PlenarprotokollTextListResponse,
        )


class PlenarprotokollTextResourceWithRawResponse:
    def __init__(self, plenarprotokoll_text: PlenarprotokollTextResource) -> None:
        self._plenarprotokoll_text = plenarprotokoll_text

        self.retrieve = to_raw_response_wrapper(
            plenarprotokoll_text.retrieve,
        )
        self.list = to_raw_response_wrapper(
            plenarprotokoll_text.list,
        )


class AsyncPlenarprotokollTextResourceWithRawResponse:
    def __init__(self, plenarprotokoll_text: AsyncPlenarprotokollTextResource) -> None:
        self._plenarprotokoll_text = plenarprotokoll_text

        self.retrieve = async_to_raw_response_wrapper(
            plenarprotokoll_text.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            plenarprotokoll_text.list,
        )


class PlenarprotokollTextResourceWithStreamingResponse:
    def __init__(self, plenarprotokoll_text: PlenarprotokollTextResource) -> None:
        self._plenarprotokoll_text = plenarprotokoll_text

        self.retrieve = to_streamed_response_wrapper(
            plenarprotokoll_text.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            plenarprotokoll_text.list,
        )


class AsyncPlenarprotokollTextResourceWithStreamingResponse:
    def __init__(self, plenarprotokoll_text: AsyncPlenarprotokollTextResource) -> None:
        self._plenarprotokoll_text = plenarprotokoll_text

        self.retrieve = async_to_streamed_response_wrapper(
            plenarprotokoll_text.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            plenarprotokoll_text.list,
        )
