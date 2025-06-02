# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from .._models import BaseModel
from .bundesland import Bundesland

__all__ = ["Person", "PersonRole"]


class PersonRole(BaseModel):
    funktion: str

    nachname: str

    vorname: str

    bundesland: Optional[Bundesland] = None
    """
    Das Bundesland wird bei persönlichen Urhebern verwendet, die Mitglieder des
    Bundesrates sind, z. B. „Reinhold Hilbers, MdBR (Finanzminister), Niedersachsen“
    """

    fraktion: Optional[str] = None

    funktionszusatz: Optional[str] = None

    namenszusatz: Optional[str] = None

    ressort_titel: Optional[str] = None

    wahlkreiszusatz: Optional[str] = None

    wahlperiode_nummer: Optional[List[int]] = None
    """Wahlperioden, für die der Personeneintrag zutrifft"""


class Person(BaseModel):
    id: str

    aktualisiert: datetime
    """Letzte Aktualisierung der Entität"""

    funktion: str

    nachname: str

    titel: str

    typ: str

    vorname: str

    basisdatum: Optional[date] = None
    """Datum des ersten zugehörigen Dokuments"""

    bundesland: Optional[Bundesland] = None
    """
    Das Bundesland wird bei persönlichen Urhebern verwendet, die Mitglieder des
    Bundesrates sind, z. B. „Reinhold Hilbers, MdBR (Finanzminister), Niedersachsen“
    """

    datum: Optional[date] = None
    """Datum des letzten zugehörigen Dokuments"""

    fraktion: Optional[str] = None

    funktionszusatz: Optional[str] = None

    namenszusatz: Optional[str] = None

    person_roles: Optional[List[PersonRole]] = None
    """Nebeneinträge mit bspw. abweichenden Funktionen oder Namensänderungen"""

    ressort: Optional[str] = None

    wahlkreiszusatz: Optional[str] = None

    wahlperiode: Optional[List[int]] = None
    """Wahlperioden aller zugehörigen Dokumente"""
