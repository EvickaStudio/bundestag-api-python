# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .ressort import Ressort
from .urheber import Urheber
from .._models import BaseModel
from .fundstelle import Fundstelle
from .vorgangsbezug import Vorgangsbezug

__all__ = ["Drucksache", "AutorenAnzeige"]


class AutorenAnzeige(BaseModel):
    id: str
    """ID von Personenstammdaten"""

    autor_titel: str

    title: str


class Drucksache(BaseModel):
    id: str

    aktualisiert: datetime
    """Letzte Aktualisierung der Entität"""

    autoren_anzahl: int
    """Gesamtzahl der Autor:innen"""

    datum: date

    dokumentart: Literal["Drucksache"]

    dokumentnummer: str

    drucksachetyp: str

    fundstelle: Fundstelle
    """
    Liefert im Vorgangsablauf das zu einem Vorgangsschritt gehörende Dokument
    (Drucksache oder Protokoll).

    Beispiel: „BT-Drucksache 19/1 (Antrag Fraktion der CDU/CSU)“ oder beim
    Vorgangsschritt Beratung „BT-Plenarprotokoll 19/1, S. 4C-12A“.
    """

    herausgeber: Literal["BT", "BR"]

    titel: str

    typ: Literal["Dokument"]

    vorgangsbezug_anzahl: int
    """Gesamtzahl der zugehörigen Vorgänge"""

    anlagen: Optional[str] = None

    autoren_anzeige: Optional[List[AutorenAnzeige]] = None
    """Zusammenfassung der ersten 4 zur Anzeige markierten Autor:innen"""

    pdf_hash: Optional[str] = None
    """MD5-Prüfsumme der PDF-Datei"""

    ressort: Optional[List[Ressort]] = None

    urheber: Optional[List[Urheber]] = None

    vorgangsbezug: Optional[List[Vorgangsbezug]] = None
    """Zusammenfassung der ersten 4 zugehörigen Vorgänge"""

    wahlperiode: Optional[int] = None
