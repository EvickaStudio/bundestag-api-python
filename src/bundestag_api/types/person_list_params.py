# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PersonListParams", "F"]


class PersonListParams(TypedDict, total=False):
    cursor: str
    """Position des Cursors zur Anfrage weiterer Entitäten

    Übersteigt die Anzahl der gefundenen Entitäten das jeweilige Limit, muss eine
    Folgeanfrage gestellt werden, um weitere Entitäten zu laden. Eine Folgeanfrage
    wird gebildet, indem alle Parameter der ursprünglichen Anfrage wiederholt werden
    und zusätzlich der cursor Parameter der letzten Antwort eingesetzt wird. Es
    können solange Folgeanfragen gestellt werden, bis sich der cursor nicht mehr
    ändert. Dies signalisiert, dass alle Entitäten geladen wurden.
    """

    f: F

    format: Literal["json", "xml"]
    """
    Steuert das Datenformat der Antwort, möglich sind JSON (voreingestellt) oder
    XML.
    """


class F(TypedDict, total=False):
    id: Iterable[int]
    """ID der Entität

    Kann wiederholt werden, um mehrere Entitäten zu selektieren.
    """

    aktualisiert: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Spätestes Aktualisierungsdatum der Entität

    Selektiert Entitäten in einem Datumsbereich basierend auf dem letzten
    Aktualisierungsdatum.
    """

    datum: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Spätestes Datum der Entität

    Selektiert Entitäten in einem Datumsbereich basierend auf dem Dokumentdatum. Für
    Vorgänge und Personen wird der Datumsbereich aller zugehörigen Dokumente
    herangezogen.
    """

    person: List[str]
    """Name einer Person

    Selektiert alle Entitäten, die den angegebenen Suchbegriff als Vor- oder
    Nachname einer Person enthalten. Kann wiederholt werden, um mehrere Namen zu
    suchen. Hinterlegt ist eine ODER-Suche. Eine Einzelwortsuche nach einem
    vollständig ausgeschriebenen Namensbestandteil ist möglich. Mehrere Suchbegriffe
    hintereinander werden als Phrase in der Reihenfolge "Nachname Vorname" gesucht.
    """

    wahlperiode: Iterable[int]
    """Nummer der Wahlperiode

    Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann
    wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine
    ODER-Suche.
    """
