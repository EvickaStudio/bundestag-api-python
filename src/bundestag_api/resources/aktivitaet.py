# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import aktivitaet_list_params, aktivitaet_retrieve_params
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
from ..types.aktivitaet import Aktivitaet
from ..types.aktivitaet_list_response import AktivitaetListResponse

__all__ = ["AktivitaetResource", "AsyncAktivitaetResource"]


class AktivitaetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AktivitaetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EvickaStudio/bundestag-api-python#accessing-raw-response-data-eg-headers
        """
        return AktivitaetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AktivitaetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EvickaStudio/bundestag-api-python#with_streaming_response
        """
        return AktivitaetResourceWithStreamingResponse(self)

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
    ) -> Aktivitaet:
        """
        Liefert Metadaten zu einer Aktivität

        Args:
          format: Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder
              XML.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/aktivitaet/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, aktivitaet_retrieve_params.AktivitaetRetrieveParams),
            ),
            cast_to=Aktivitaet,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        f: aktivitaet_list_params.F | NotGiven = NOT_GIVEN,
        format: Literal["json", "xml"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AktivitaetListResponse:
        """
        Liefert eine Liste von Metadaten zu Aktivitäten

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
            "/aktivitaet",
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
                    aktivitaet_list_params.AktivitaetListParams,
                ),
            ),
            cast_to=AktivitaetListResponse,
        )


class AsyncAktivitaetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAktivitaetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/EvickaStudio/bundestag-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAktivitaetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAktivitaetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/EvickaStudio/bundestag-api-python#with_streaming_response
        """
        return AsyncAktivitaetResourceWithStreamingResponse(self)

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
    ) -> Aktivitaet:
        """
        Liefert Metadaten zu einer Aktivität

        Args:
          format: Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder
              XML.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/aktivitaet/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"format": format}, aktivitaet_retrieve_params.AktivitaetRetrieveParams
                ),
            ),
            cast_to=Aktivitaet,
        )

    async def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        f: aktivitaet_list_params.F | NotGiven = NOT_GIVEN,
        format: Literal["json", "xml"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AktivitaetListResponse:
        """
        Liefert eine Liste von Metadaten zu Aktivitäten

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
            "/aktivitaet",
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
                    aktivitaet_list_params.AktivitaetListParams,
                ),
            ),
            cast_to=AktivitaetListResponse,
        )


class AktivitaetResourceWithRawResponse:
    def __init__(self, aktivitaet: AktivitaetResource) -> None:
        self._aktivitaet = aktivitaet

        self.retrieve = to_raw_response_wrapper(
            aktivitaet.retrieve,
        )
        self.list = to_raw_response_wrapper(
            aktivitaet.list,
        )


class AsyncAktivitaetResourceWithRawResponse:
    def __init__(self, aktivitaet: AsyncAktivitaetResource) -> None:
        self._aktivitaet = aktivitaet

        self.retrieve = async_to_raw_response_wrapper(
            aktivitaet.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            aktivitaet.list,
        )


class AktivitaetResourceWithStreamingResponse:
    def __init__(self, aktivitaet: AktivitaetResource) -> None:
        self._aktivitaet = aktivitaet

        self.retrieve = to_streamed_response_wrapper(
            aktivitaet.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            aktivitaet.list,
        )


class AsyncAktivitaetResourceWithStreamingResponse:
    def __init__(self, aktivitaet: AsyncAktivitaetResource) -> None:
        self._aktivitaet = aktivitaet

        self.retrieve = async_to_streamed_response_wrapper(
            aktivitaet.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            aktivitaet.list,
        )
