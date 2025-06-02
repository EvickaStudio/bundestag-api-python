# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from bundestag_api import BundestagAPI, AsyncBundestagAPI
from bundestag_api.types import (
    PlenarprotokollText,
    PlenarprotokollTextListResponse,
)
from bundestag_api._utils import parse_date, parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlenarprotokollText:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: BundestagAPI) -> None:
        plenarprotokoll_text = client.plenarprotokoll_text.retrieve(
            id=1,
        )
        assert_matches_type(PlenarprotokollText, plenarprotokoll_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: BundestagAPI) -> None:
        plenarprotokoll_text = client.plenarprotokoll_text.retrieve(
            id=1,
            format="json",
        )
        assert_matches_type(PlenarprotokollText, plenarprotokoll_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: BundestagAPI) -> None:
        response = client.plenarprotokoll_text.with_raw_response.retrieve(
            id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plenarprotokoll_text = response.parse()
        assert_matches_type(PlenarprotokollText, plenarprotokoll_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: BundestagAPI) -> None:
        with client.plenarprotokoll_text.with_streaming_response.retrieve(
            id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plenarprotokoll_text = response.parse()
            assert_matches_type(PlenarprotokollText, plenarprotokoll_text, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: BundestagAPI) -> None:
        plenarprotokoll_text = client.plenarprotokoll_text.list()
        assert_matches_type(PlenarprotokollTextListResponse, plenarprotokoll_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: BundestagAPI) -> None:
        plenarprotokoll_text = client.plenarprotokoll_text.list(
            cursor="cursor",
            f={
                "id": [0],
                "aktualisiert": parse_datetime("2019-12-27T18:11:19.117Z"),
                "datum": parse_date("2019-12-27"),
                "dokumentnummer": [""],
                "vorgangstyp": [""],
                "vorgangstyp_notation": [0],
                "wahlperiode": [0],
                "zuordnung": "BT",
            },
            format="json",
        )
        assert_matches_type(PlenarprotokollTextListResponse, plenarprotokoll_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: BundestagAPI) -> None:
        response = client.plenarprotokoll_text.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plenarprotokoll_text = response.parse()
        assert_matches_type(PlenarprotokollTextListResponse, plenarprotokoll_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: BundestagAPI) -> None:
        with client.plenarprotokoll_text.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plenarprotokoll_text = response.parse()
            assert_matches_type(PlenarprotokollTextListResponse, plenarprotokoll_text, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPlenarprotokollText:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBundestagAPI) -> None:
        plenarprotokoll_text = await async_client.plenarprotokoll_text.retrieve(
            id=1,
        )
        assert_matches_type(PlenarprotokollText, plenarprotokoll_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBundestagAPI) -> None:
        plenarprotokoll_text = await async_client.plenarprotokoll_text.retrieve(
            id=1,
            format="json",
        )
        assert_matches_type(PlenarprotokollText, plenarprotokoll_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBundestagAPI) -> None:
        response = await async_client.plenarprotokoll_text.with_raw_response.retrieve(
            id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plenarprotokoll_text = await response.parse()
        assert_matches_type(PlenarprotokollText, plenarprotokoll_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBundestagAPI) -> None:
        async with async_client.plenarprotokoll_text.with_streaming_response.retrieve(
            id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plenarprotokoll_text = await response.parse()
            assert_matches_type(PlenarprotokollText, plenarprotokoll_text, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBundestagAPI) -> None:
        plenarprotokoll_text = await async_client.plenarprotokoll_text.list()
        assert_matches_type(PlenarprotokollTextListResponse, plenarprotokoll_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBundestagAPI) -> None:
        plenarprotokoll_text = await async_client.plenarprotokoll_text.list(
            cursor="cursor",
            f={
                "id": [0],
                "aktualisiert": parse_datetime("2019-12-27T18:11:19.117Z"),
                "datum": parse_date("2019-12-27"),
                "dokumentnummer": [""],
                "vorgangstyp": [""],
                "vorgangstyp_notation": [0],
                "wahlperiode": [0],
                "zuordnung": "BT",
            },
            format="json",
        )
        assert_matches_type(PlenarprotokollTextListResponse, plenarprotokoll_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBundestagAPI) -> None:
        response = await async_client.plenarprotokoll_text.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plenarprotokoll_text = await response.parse()
        assert_matches_type(PlenarprotokollTextListResponse, plenarprotokoll_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBundestagAPI) -> None:
        async with async_client.plenarprotokoll_text.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plenarprotokoll_text = await response.parse()
            assert_matches_type(PlenarprotokollTextListResponse, plenarprotokoll_text, path=["response"])

        assert cast(Any, response.is_closed) is True
