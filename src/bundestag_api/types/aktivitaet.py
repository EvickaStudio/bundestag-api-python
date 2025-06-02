# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .deskriptor import Deskriptor
from .fundstelle import Fundstelle
from .vorgangspositionbezug import Vorgangspositionbezug

__all__ = ["Aktivitaet"]


class Aktivitaet(BaseModel):
    id: str

    aktivitaetsart: str

    aktualisiert: datetime
    """Letzte Aktualisierung der Entität oder des zugehörigen Dokuments"""

    datum: date

    dokumentart: Literal["Drucksache", "Plenarprotokoll"]

    fundstelle: Fundstelle
    """
    Liefert im Vorgangsablauf das zu einem Vorgangsschritt gehörende Dokument
    (Drucksache oder Protokoll).

    Beispiel: „BT-Drucksache 19/1 (Antrag Fraktion der CDU/CSU)“ oder beim
    Vorgangsschritt Beratung „BT-Plenarprotokoll 19/1, S. 4C-12A“.
    """

    person_id: str
    """ID des Haupteintrags der zugehörigen Personenstammdaten"""

    titel: str

    typ: Literal["Aktivität"]

    vorgangsbezug_anzahl: int
    """Gesamtzahl der zugehörigen Vorgänge"""

    wahlperiode: int

    abstract: Optional[str] = None

    deskriptor: Optional[List[Deskriptor]] = None

    vorgangsbezug: Optional[List[Vorgangspositionbezug]] = None
    """Zusammenfassung der ersten 4 zugehörigen Vorgänge"""
