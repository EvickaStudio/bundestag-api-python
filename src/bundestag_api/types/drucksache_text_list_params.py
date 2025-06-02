# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .zuordnung import Zuordnung

__all__ = ["DrucksacheTextListParams", "F"]


class DrucksacheTextListParams(TypedDict, total=False):
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

    dokumentnummer: List[str]
    """Dokumentnummer einer Drucksache oder eines Plenarprotokolls

    Selektiert alle Entitäten, die mit der angegebenen Dokumentnummer verknüpft
    sind. Kann wiederholt werden, um mehrere Dokumentnummern zu selektieren.
    Hinterlegt ist eine ODER-Suche.
    """

    drucksachetyp: str
    """Typ der Drucksache

    Selektiert alle Entitäten, die mit dem angegebenen Drucksachetyp verknüpft sind.
    """

    ressort_fdf: List[str]
    """Ressort (federführend)

    Selektiert alle Entitäten, die mit dem angegebenen federführenden Ressort in
    einer Drucksache verknüpft sind. Kann wiederholt werden, um die Schnittmenge
    mehrerer Ressorts zu selektieren. Hinterlegt ist eine UND-Suche. Eine ODER-Suche
    über mehrere federführende Ressorts ist mit einer einzigen Abfrage nicht
    möglich. Die federführenden Ressorts müssen dazu einzeln abgefragt werden.
    """

    titel: List[str]
    """Titel

    Selektiert alle Entitäten, die den angegebenen Suchbegriff im Titel enthalten.
    Kann wiederholt werden, um mehrere Titel zu selektieren. Hinterlegt ist eine
    ODER-Suche. Eine Einzelwortsuche ist möglich. Mehrere Suchbegriffe
    hintereinander werden als Phrase gesucht.
    """

    urheber: List[str]
    """Urheber

    Selektiert alle Entitäten, die mit dem angegebenen Urheber in einer Drucksache
    verknüpft sind. Kann wiederholt werden, um die Schnittmenge mehrerer Urheber zu
    selektieren. Hinterlegt ist eine UND-Suche. Eine ODER-Suche über mehrere Urheber
    ist mit einer einzigen Abfrage nicht möglich. Die Urheber müssen dazu einzeln
    abgefragt werden.
    """

    vorgangstyp: List[str]
    """Vorgangstyp

    Selektiert alle Entitäten, die dem angegebenen Vorgangstyp zugeordnet sind. Kann
    wiederholt werden, um mehrere Vorgangstypen zu selektieren. Hinterlegt ist eine
    ODER-Suche.
    """

    vorgangstyp_notation: Iterable[int]
    """Vorgangstyp-Notation

    Selektiert alle Entitäten, die der angegebenen Vorgangstyp-Notation zugeordnet
    sind. Kann wiederholt werden, um mehrere Vorgangstypen zu selektieren.
    Hinterlegt ist eine ODER-Suche.
    """

    wahlperiode: Iterable[int]
    """Nummer der Wahlperiode

    Selektiert alle Entitäten, die der angegebenen Wahlperiode zugeordnet sind. Kann
    wiederholt werden, um mehrere Wahlperioden zu selektieren. Hinterlegt ist eine
    ODER-Suche.
    """

    zuordnung: Zuordnung
    """
    Zuordnung der Entität zum Bundestag, Bundesrat, Bundesversammlung oder
    Europakammer
    """
