# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    person,
    vorgang,
    aktivitaet,
    drucksache,
    drucksache_text,
    plenarprotokoll,
    vorgangsposition,
    plenarprotokoll_text,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "BundestagAPI",
    "AsyncBundestagAPI",
    "Client",
    "AsyncClient",
]


class BundestagAPI(SyncAPIClient):
    vorgang: vorgang.VorgangResource
    vorgangsposition: vorgangsposition.VorgangspositionResource
    drucksache: drucksache.DrucksacheResource
    drucksache_text: drucksache_text.DrucksacheTextResource
    plenarprotokoll: plenarprotokoll.PlenarprotokollResource
    plenarprotokoll_text: plenarprotokoll_text.PlenarprotokollTextResource
    aktivitaet: aktivitaet.AktivitaetResource
    person: person.PersonResource
    with_raw_response: BundestagAPIWithRawResponse
    with_streaming_response: BundestagAPIWithStreamedResponse

    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous BundestagAPI client instance.

        This automatically infers the `api_key` argument from the `BUNDESTAG_API_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BUNDESTAG_API_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BUNDESTAG_API_BASE_URL")
        if base_url is None:
            base_url = f"https://search.dip.bundestag.de/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.vorgang = vorgang.VorgangResource(self)
        self.vorgangsposition = vorgangsposition.VorgangspositionResource(self)
        self.drucksache = drucksache.DrucksacheResource(self)
        self.drucksache_text = drucksache_text.DrucksacheTextResource(self)
        self.plenarprotokoll = plenarprotokoll.PlenarprotokollResource(self)
        self.plenarprotokoll_text = plenarprotokoll_text.PlenarprotokollTextResource(self)
        self.aktivitaet = aktivitaet.AktivitaetResource(self)
        self.person = person.PersonResource(self)
        self.with_raw_response = BundestagAPIWithRawResponse(self)
        self.with_streaming_response = BundestagAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"ApiKey {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBundestagAPI(AsyncAPIClient):
    vorgang: vorgang.AsyncVorgangResource
    vorgangsposition: vorgangsposition.AsyncVorgangspositionResource
    drucksache: drucksache.AsyncDrucksacheResource
    drucksache_text: drucksache_text.AsyncDrucksacheTextResource
    plenarprotokoll: plenarprotokoll.AsyncPlenarprotokollResource
    plenarprotokoll_text: plenarprotokoll_text.AsyncPlenarprotokollTextResource
    aktivitaet: aktivitaet.AsyncAktivitaetResource
    person: person.AsyncPersonResource
    with_raw_response: AsyncBundestagAPIWithRawResponse
    with_streaming_response: AsyncBundestagAPIWithStreamedResponse

    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncBundestagAPI client instance.

        This automatically infers the `api_key` argument from the `BUNDESTAG_API_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BUNDESTAG_API_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BUNDESTAG_API_BASE_URL")
        if base_url is None:
            base_url = f"https://search.dip.bundestag.de/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.vorgang = vorgang.AsyncVorgangResource(self)
        self.vorgangsposition = vorgangsposition.AsyncVorgangspositionResource(self)
        self.drucksache = drucksache.AsyncDrucksacheResource(self)
        self.drucksache_text = drucksache_text.AsyncDrucksacheTextResource(self)
        self.plenarprotokoll = plenarprotokoll.AsyncPlenarprotokollResource(self)
        self.plenarprotokoll_text = plenarprotokoll_text.AsyncPlenarprotokollTextResource(self)
        self.aktivitaet = aktivitaet.AsyncAktivitaetResource(self)
        self.person = person.AsyncPersonResource(self)
        self.with_raw_response = AsyncBundestagAPIWithRawResponse(self)
        self.with_streaming_response = AsyncBundestagAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BundestagAPIWithRawResponse:
    def __init__(self, client: BundestagAPI) -> None:
        self.vorgang = vorgang.VorgangResourceWithRawResponse(client.vorgang)
        self.vorgangsposition = vorgangsposition.VorgangspositionResourceWithRawResponse(client.vorgangsposition)
        self.drucksache = drucksache.DrucksacheResourceWithRawResponse(client.drucksache)
        self.drucksache_text = drucksache_text.DrucksacheTextResourceWithRawResponse(client.drucksache_text)
        self.plenarprotokoll = plenarprotokoll.PlenarprotokollResourceWithRawResponse(client.plenarprotokoll)
        self.plenarprotokoll_text = plenarprotokoll_text.PlenarprotokollTextResourceWithRawResponse(
            client.plenarprotokoll_text
        )
        self.aktivitaet = aktivitaet.AktivitaetResourceWithRawResponse(client.aktivitaet)
        self.person = person.PersonResourceWithRawResponse(client.person)


class AsyncBundestagAPIWithRawResponse:
    def __init__(self, client: AsyncBundestagAPI) -> None:
        self.vorgang = vorgang.AsyncVorgangResourceWithRawResponse(client.vorgang)
        self.vorgangsposition = vorgangsposition.AsyncVorgangspositionResourceWithRawResponse(client.vorgangsposition)
        self.drucksache = drucksache.AsyncDrucksacheResourceWithRawResponse(client.drucksache)
        self.drucksache_text = drucksache_text.AsyncDrucksacheTextResourceWithRawResponse(client.drucksache_text)
        self.plenarprotokoll = plenarprotokoll.AsyncPlenarprotokollResourceWithRawResponse(client.plenarprotokoll)
        self.plenarprotokoll_text = plenarprotokoll_text.AsyncPlenarprotokollTextResourceWithRawResponse(
            client.plenarprotokoll_text
        )
        self.aktivitaet = aktivitaet.AsyncAktivitaetResourceWithRawResponse(client.aktivitaet)
        self.person = person.AsyncPersonResourceWithRawResponse(client.person)


class BundestagAPIWithStreamedResponse:
    def __init__(self, client: BundestagAPI) -> None:
        self.vorgang = vorgang.VorgangResourceWithStreamingResponse(client.vorgang)
        self.vorgangsposition = vorgangsposition.VorgangspositionResourceWithStreamingResponse(client.vorgangsposition)
        self.drucksache = drucksache.DrucksacheResourceWithStreamingResponse(client.drucksache)
        self.drucksache_text = drucksache_text.DrucksacheTextResourceWithStreamingResponse(client.drucksache_text)
        self.plenarprotokoll = plenarprotokoll.PlenarprotokollResourceWithStreamingResponse(client.plenarprotokoll)
        self.plenarprotokoll_text = plenarprotokoll_text.PlenarprotokollTextResourceWithStreamingResponse(
            client.plenarprotokoll_text
        )
        self.aktivitaet = aktivitaet.AktivitaetResourceWithStreamingResponse(client.aktivitaet)
        self.person = person.PersonResourceWithStreamingResponse(client.person)


class AsyncBundestagAPIWithStreamedResponse:
    def __init__(self, client: AsyncBundestagAPI) -> None:
        self.vorgang = vorgang.AsyncVorgangResourceWithStreamingResponse(client.vorgang)
        self.vorgangsposition = vorgangsposition.AsyncVorgangspositionResourceWithStreamingResponse(
            client.vorgangsposition
        )
        self.drucksache = drucksache.AsyncDrucksacheResourceWithStreamingResponse(client.drucksache)
        self.drucksache_text = drucksache_text.AsyncDrucksacheTextResourceWithStreamingResponse(client.drucksache_text)
        self.plenarprotokoll = plenarprotokoll.AsyncPlenarprotokollResourceWithStreamingResponse(client.plenarprotokoll)
        self.plenarprotokoll_text = plenarprotokoll_text.AsyncPlenarprotokollTextResourceWithStreamingResponse(
            client.plenarprotokoll_text
        )
        self.aktivitaet = aktivitaet.AsyncAktivitaetResourceWithStreamingResponse(client.aktivitaet)
        self.person = person.AsyncPersonResourceWithStreamingResponse(client.person)


Client = BundestagAPI

AsyncClient = AsyncBundestagAPI
