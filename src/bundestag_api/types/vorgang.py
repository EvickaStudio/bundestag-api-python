# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from . import deskriptor
from .._models import BaseModel

__all__ = ["Vorgang", "Deskriptor", "Inkrafttreten", "Verkuendung", "VorgangVerlinkung"]


class Deskriptor(deskriptor.Deskriptor):
    fundstelle: bool
    """Kennzeichnet Deskriptoren mit zentraler Bedeutung"""


class Inkrafttreten(BaseModel):
    datum: date

    erlaeuterung: Optional[str] = None


class Verkuendung(BaseModel):
    ausfertigungsdatum: date

    einleitungstext: str

    fundstelle: str

    jahrgang: str

    seite: str

    verkuendungsdatum: date

    heftnummer: Optional[str] = None

    pdf_url: Optional[str] = None

    rubrik_nr: Optional[str] = None

    titel: Optional[str] = None

    verkuendungsblatt_bezeichnung: Optional[str] = None

    verkuendungsblatt_kuerzel: Optional[str] = None


class VorgangVerlinkung(BaseModel):
    id: str
    """ID eines verknüpften Vorgangs"""

    titel: str

    verweisung: str

    wahlperiode: int

    gesta: Optional[str] = None


class Vorgang(BaseModel):
    id: str

    aktualisiert: datetime
    """Letzte Aktualisierung der Entität"""

    titel: str

    typ: Literal["Vorgang"]

    vorgangstyp: str

    wahlperiode: int

    abstract: Optional[str] = None

    archiv: Optional[str] = None
    """Archivsignatur"""

    beratungsstand: Optional[str] = None

    datum: Optional[date] = None
    """Datierung des letzten zugehörigen Dokuments"""

    deskriptor: Optional[List[Deskriptor]] = None

    gesta: Optional[str] = None
    """GESTA-Ordnungsnummer"""

    initiative: Optional[List[str]] = None

    inkrafttreten: Optional[List[Inkrafttreten]] = None

    kom: Optional[str] = None
    """KOM-Nr."""

    mitteilung: Optional[str] = None

    ratsdok: Optional[str] = None
    """Ratsdok-Nr."""

    sachgebiet: Optional[List[str]] = None

    sek: Optional[str] = None
    """SEK-Nr."""

    verkuendung: Optional[List[Verkuendung]] = None

    vorgang_verlinkung: Optional[List[VorgangVerlinkung]] = None

    zustimmungsbeduerftigkeit: Optional[List[str]] = None
