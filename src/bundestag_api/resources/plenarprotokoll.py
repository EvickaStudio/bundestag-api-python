# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import plenarprotokoll_list_params, plenarprotokoll_retrieve_params
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
from ..types.plenarprotokoll import Plenarprotokoll
from ..types.plenarprotokoll_list_response import PlenarprotokollListResponse

__all__ = ["PlenarprotokollResource", "AsyncPlenarprotokollResource"]


class PlenarprotokollResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlenarprotokollResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bundestag-api-python#accessing-raw-response-data-eg-headers
        """
        return PlenarprotokollResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlenarprotokollResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bundestag-api-python#with_streaming_response
        """
        return PlenarprotokollResourceWithStreamingResponse(self)

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
    ) -> Plenarprotokoll:
        """
        Liefert Metadaten zu einem Plenarprotokoll

        Args:
          format: Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder
              XML.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/plenarprotokoll/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"format": format}, plenarprotokoll_retrieve_params.PlenarprotokollRetrieveParams
                ),
            ),
            cast_to=Plenarprotokoll,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        f: plenarprotokoll_list_params.F | NotGiven = NOT_GIVEN,
        format: Literal["json", "xml"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlenarprotokollListResponse:
        """
        Liefert eine Liste von Metadaten zu Plenarprotokollen

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
            "/plenarprotokoll",
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
                    plenarprotokoll_list_params.PlenarprotokollListParams,
                ),
            ),
            cast_to=PlenarprotokollListResponse,
        )


class AsyncPlenarprotokollResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlenarprotokollResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bundestag-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlenarprotokollResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlenarprotokollResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bundestag-api-python#with_streaming_response
        """
        return AsyncPlenarprotokollResourceWithStreamingResponse(self)

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
    ) -> Plenarprotokoll:
        """
        Liefert Metadaten zu einem Plenarprotokoll

        Args:
          format: Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder
              XML.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/plenarprotokoll/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"format": format}, plenarprotokoll_retrieve_params.PlenarprotokollRetrieveParams
                ),
            ),
            cast_to=Plenarprotokoll,
        )

    async def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        f: plenarprotokoll_list_params.F | NotGiven = NOT_GIVEN,
        format: Literal["json", "xml"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlenarprotokollListResponse:
        """
        Liefert eine Liste von Metadaten zu Plenarprotokollen

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
            "/plenarprotokoll",
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
                    plenarprotokoll_list_params.PlenarprotokollListParams,
                ),
            ),
            cast_to=PlenarprotokollListResponse,
        )


class PlenarprotokollResourceWithRawResponse:
    def __init__(self, plenarprotokoll: PlenarprotokollResource) -> None:
        self._plenarprotokoll = plenarprotokoll

        self.retrieve = to_raw_response_wrapper(
            plenarprotokoll.retrieve,
        )
        self.list = to_raw_response_wrapper(
            plenarprotokoll.list,
        )


class AsyncPlenarprotokollResourceWithRawResponse:
    def __init__(self, plenarprotokoll: AsyncPlenarprotokollResource) -> None:
        self._plenarprotokoll = plenarprotokoll

        self.retrieve = async_to_raw_response_wrapper(
            plenarprotokoll.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            plenarprotokoll.list,
        )


class PlenarprotokollResourceWithStreamingResponse:
    def __init__(self, plenarprotokoll: PlenarprotokollResource) -> None:
        self._plenarprotokoll = plenarprotokoll

        self.retrieve = to_streamed_response_wrapper(
            plenarprotokoll.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            plenarprotokoll.list,
        )


class AsyncPlenarprotokollResourceWithStreamingResponse:
    def __init__(self, plenarprotokoll: AsyncPlenarprotokollResource) -> None:
        self._plenarprotokoll = plenarprotokoll

        self.retrieve = async_to_streamed_response_wrapper(
            plenarprotokoll.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            plenarprotokoll.list,
        )
