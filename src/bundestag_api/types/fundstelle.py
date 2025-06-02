# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel
from .quadrant import Quadrant
from .zuordnung import Zuordnung

__all__ = ["Fundstelle"]


class Fundstelle(BaseModel):
    id: str
    """ID einer Drucksache oder eines Plenarprotokolls"""

    datum: date

    dokumentart: Literal["Drucksache", "Plenarprotokoll"]

    dokumentnummer: str

    herausgeber: Zuordnung
    """
    Jeder Vorgangsschritt ist entweder dem Bundestag (BT), dem Bundesrat (BR), der
    Bundesversammlung (BV) oder der Europakammer (EK) zugeordnet. Über die Zuordnung
    lassen sich bspw. Rechtsverordnungen herausfiltern, an denen der Bundestag
    beteiligt / nicht beteiligt war.
    """

    urheber: List[str]

    anfangsquadrant: Optional[Quadrant] = None
    """Teil der Fundstelle eines Plenarprotokolls.

    Jede Seite im Plenarprotokoll ist in vier gleich große Viertel unterteilt
    (Quadranten) mit den Bezeichnungen A, B, C, D.
    """

    anfangsseite: Optional[int] = None

    anlagen: Optional[str] = None

    drucksachetyp: Optional[str] = None

    endquadrant: Optional[Quadrant] = None
    """Teil der Fundstelle eines Plenarprotokolls.

    Jede Seite im Plenarprotokoll ist in vier gleich große Viertel unterteilt
    (Quadranten) mit den Bezeichnungen A, B, C, D.
    """

    endseite: Optional[int] = None

    frage_nummer: Optional[str] = None

    pdf_url: Optional[str] = None

    seite: Optional[str] = None

    top: Optional[int] = None

    top_zusatz: Optional[str] = None

    verteildatum: Optional[date] = None

    xml_url: Optional[str] = None
    """
    Strukturierte XML-Version des Dokuments (aktuell nur für BT-Plenarprotokolle ab
    WP 18 verfügbar)
    """
