# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import drucksache_list_params, drucksache_retrieve_params
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
from ..types.drucksache import Drucksache
from ..types.drucksache_list_response import DrucksacheListResponse

__all__ = ["DrucksacheResource", "AsyncDrucksacheResource"]


class DrucksacheResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DrucksacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bundestag-api-python#accessing-raw-response-data-eg-headers
        """
        return DrucksacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DrucksacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bundestag-api-python#with_streaming_response
        """
        return DrucksacheResourceWithStreamingResponse(self)

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
    ) -> Drucksache:
        """
        Liefert Metadaten zu einer Drucksache

        Args:
          format: Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder
              XML.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/drucksache/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, drucksache_retrieve_params.DrucksacheRetrieveParams),
            ),
            cast_to=Drucksache,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        f: drucksache_list_params.F | NotGiven = NOT_GIVEN,
        format: Literal["json", "xml"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DrucksacheListResponse:
        """
        Liefert eine Liste von Metadaten zu Drucksachen

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
            "/drucksache",
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
                    drucksache_list_params.DrucksacheListParams,
                ),
            ),
            cast_to=DrucksacheListResponse,
        )


class AsyncDrucksacheResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDrucksacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bundestag-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDrucksacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDrucksacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bundestag-api-python#with_streaming_response
        """
        return AsyncDrucksacheResourceWithStreamingResponse(self)

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
    ) -> Drucksache:
        """
        Liefert Metadaten zu einer Drucksache

        Args:
          format: Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder
              XML.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/drucksache/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"format": format}, drucksache_retrieve_params.DrucksacheRetrieveParams
                ),
            ),
            cast_to=Drucksache,
        )

    async def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        f: drucksache_list_params.F | NotGiven = NOT_GIVEN,
        format: Literal["json", "xml"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DrucksacheListResponse:
        """
        Liefert eine Liste von Metadaten zu Drucksachen

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
            "/drucksache",
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
                    drucksache_list_params.DrucksacheListParams,
                ),
            ),
            cast_to=DrucksacheListResponse,
        )


class DrucksacheResourceWithRawResponse:
    def __init__(self, drucksache: DrucksacheResource) -> None:
        self._drucksache = drucksache

        self.retrieve = to_raw_response_wrapper(
            drucksache.retrieve,
        )
        self.list = to_raw_response_wrapper(
            drucksache.list,
        )


class AsyncDrucksacheResourceWithRawResponse:
    def __init__(self, drucksache: AsyncDrucksacheResource) -> None:
        self._drucksache = drucksache

        self.retrieve = async_to_raw_response_wrapper(
            drucksache.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            drucksache.list,
        )


class DrucksacheResourceWithStreamingResponse:
    def __init__(self, drucksache: DrucksacheResource) -> None:
        self._drucksache = drucksache

        self.retrieve = to_streamed_response_wrapper(
            drucksache.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            drucksache.list,
        )


class AsyncDrucksacheResourceWithStreamingResponse:
    def __init__(self, drucksache: AsyncDrucksacheResource) -> None:
        self._drucksache = drucksache

        self.retrieve = async_to_streamed_response_wrapper(
            drucksache.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            drucksache.list,
        )
