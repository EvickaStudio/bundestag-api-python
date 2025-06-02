# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .zuordnung import Zuordnung
from .fundstelle import Fundstelle
from .vorgangsbezug import Vorgangsbezug

__all__ = ["Plenarprotokoll"]


class Plenarprotokoll(BaseModel):
    id: str

    aktualisiert: datetime
    """Letzte Aktualisierung der Entität"""

    datum: date

    dokumentart: Literal["Plenarprotokoll"]

    dokumentnummer: str

    fundstelle: Fundstelle
    """
    Liefert im Vorgangsablauf das zu einem Vorgangsschritt gehörende Dokument
    (Drucksache oder Protokoll).

    Beispiel: „BT-Drucksache 19/1 (Antrag Fraktion der CDU/CSU)“ oder beim
    Vorgangsschritt Beratung „BT-Plenarprotokoll 19/1, S. 4C-12A“.
    """

    herausgeber: Zuordnung
    """
    Jeder Vorgangsschritt ist entweder dem Bundestag (BT), dem Bundesrat (BR), der
    Bundesversammlung (BV) oder der Europakammer (EK) zugeordnet. Über die Zuordnung
    lassen sich bspw. Rechtsverordnungen herausfiltern, an denen der Bundestag
    beteiligt / nicht beteiligt war.
    """

    titel: str

    typ: Literal["Dokument"]

    vorgangsbezug_anzahl: int
    """Gesamtzahl der zugehörigen Vorgänge"""

    pdf_hash: Optional[str] = None
    """MD5-Prüfsumme der PDF-Datei"""

    sitzungsbemerkung: Optional[str] = None

    vorgangsbezug: Optional[List[Vorgangsbezug]] = None
    """Zusammenfassung der ersten 4 zugehörigen Vorgänge"""

    wahlperiode: Optional[int] = None
