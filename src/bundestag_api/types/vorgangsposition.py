# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .ressort import Ressort
from .urheber import Urheber
from .._models import BaseModel
from .zuordnung import Zuordnung
from .fundstelle import Fundstelle
from .vorgangspositionbezug import Vorgangspositionbezug

__all__ = ["Vorgangsposition", "AktivitaetAnzeige", "Beschlussfassung", "Ueberweisung"]


class AktivitaetAnzeige(BaseModel):
    aktivitaetsart: str

    titel: str

    pdf_url: Optional[str] = None

    seite: Optional[str] = None


class Beschlussfassung(BaseModel):
    beschlusstenor: str

    abstimm_ergebnis_bemerkung: Optional[str] = None

    abstimmungsart: Optional[
        Literal[
            "Abstimmung durch Aufruf der Länder",
            "Geheime Wahl",
            "Hammelsprung",
            "Namentliche Abstimmung",
            "Verhältniswahl",
        ]
    ] = None

    dokumentnummer: Optional[str] = None

    grundlage: Optional[str] = None

    mehrheit: Optional[Literal["Absolute Mehrheit", "Zweidrittelmehrheit"]] = None

    seite: Optional[str] = None


class Ueberweisung(BaseModel):
    ausschuss: str

    ausschuss_kuerzel: str

    federfuehrung: bool

    ueberweisungsart: Optional[str] = None


class Vorgangsposition(BaseModel):
    id: str

    aktivitaet_anzahl: int
    """Gesamtzahl der zugehörigen Aktivitäten"""

    aktualisiert: datetime
    """Letzte Aktualisierung der Entität oder des zugehörigen Dokuments"""

    datum: date
    """Datum des zugehörigen Dokuments"""

    dokumentart: Literal["Drucksache", "Plenarprotokoll"]

    fortsetzung: bool
    """
    Erstreckt sich eine Beratung über mehrere Plenarprotokolle, so müssen
    entsprechend viele Vorgangsschritte mit je gleicher Vorgangsposition im
    Vorgangsablauf angelegt werden. Der zweite und jeder weitere dieser Schritte
    wird dann als "Fortsetzung" gekennzeichnet (Attribut `fortsetzung: true`). Für
    die Beratung des Gesetzentwurfs für die Feststellung des Haushaltsplanes
    (Haushaltsberatungen) gelten abweichende Regelungen.
    """

    fundstelle: Fundstelle
    """
    Liefert im Vorgangsablauf das zu einem Vorgangsschritt gehörende Dokument
    (Drucksache oder Protokoll).

    Beispiel: „BT-Drucksache 19/1 (Antrag Fraktion der CDU/CSU)“ oder beim
    Vorgangsschritt Beratung „BT-Plenarprotokoll 19/1, S. 4C-12A“.
    """

    gang: bool
    """
    Alle Vorgangsschritte, die von besonderer Bedeutung für den Fortgang der
    Beratung sind, werden durch das Attribut `gang: true` gekennzeichnet.

    Ist ein solcher Vorgangsschritt mit einer Drucksache verknüpft, werden im
    Frontend unter der Benennung "Wichtige Drucksachen" Herausgeber, Nummer und Typ
    sowie das Datum der entsprechenden Drucksachen ausgegeben (z.B. BT-Drs 18/13014
    (Beschlussempfehlung), 28.06.2017). Ist er mit einem Plenarprotokoll verknüpft,
    werden im Frontend unter der Benennung "Plenum" der Klartext der
    Vorgangsposition, Datum, Herausgeber und Nummer des Plenarprotokolls mit
    Anfangsseite/Quadrant und Endseite/Quadrant dargestellt (z.B. 2. Beratung:
    29.06.2017, BT-PlPr 18/243, S. 24964C - 24973C).
    """

    nachtrag: bool
    """
    Eine Auswertungseinheit eines Plenarprotokolls kann nur an genau einen
    Vorgangsschritt angebunden werden. Müssen aber mehrere Auswertungseinheiten für
    einen Vorgangsschritt gebildet werden (weil die Ergänzung einer Rede erst in
    einem späteren Protokoll erscheint oder weil sich z.B. bei einer Verbundenen
    Beratung (§ 24 GO-BT) nicht alle Schriftlichen Erklärungen nach § 31 GO-BT auf
    sämtliche Vorlagen beziehen), dann müssen im Vorgangsablauf mehrere
    Vorgangsschritte mit der gleichen Vorgangsposition angelegt werden. Der zweite
    und jeder weitere dieser Schritte wird dann als "Nachtrag" gekennzeichnet
    (Attribut `nachtrag: true`)
    """

    titel: str
    """Titel des zugehörigen Vorgangs"""

    typ: Literal["Vorgangsposition"]

    vorgang_id: str
    """ID des zugehörigen Vorgangs"""

    vorgangsposition: str

    vorgangstyp: str
    """Vorgangstyp des zugehörigen Vorgangs"""

    zuordnung: Zuordnung
    """
    Jeder Vorgangsschritt ist entweder dem Bundestag (BT), dem Bundesrat (BR), der
    Bundesversammlung (BV) oder der Europakammer (EK) zugeordnet. Über die Zuordnung
    lassen sich bspw. Rechtsverordnungen herausfiltern, an denen der Bundestag
    beteiligt / nicht beteiligt war.
    """

    abstract: Optional[str] = None

    aktivitaet_anzeige: Optional[List[AktivitaetAnzeige]] = None
    """Zusammenfassung der ersten 4 zur Anzeige vorgesehenen Aktivitäten"""

    beschlussfassung: Optional[List[Beschlussfassung]] = None

    kom: Optional[str] = None
    """KOM-Nr."""

    mitberaten: Optional[List[Vorgangspositionbezug]] = None
    """Es ist eine häufig geübte Praxis, mehrere thematisch verwandte Vorlagen (z.B.

    konkurrierende Anträge der verschiedenen Fraktionen zum Thema
    Diesel-Fahrverbote) in einer Debatte gemeinsam zu beraten ("Zusammenberatung").

    `mitberaten` liefert, von einem Vorgang ausgehend, alle anderen Vorgänge, die
    Gegenstand der Zusammenberatung sind.
    """

    ratsdok: Optional[str] = None
    """Ratsdok-Nr."""

    ressort: Optional[List[Ressort]] = None

    sek: Optional[str] = None
    """SEK-Nr."""

    ueberweisung: Optional[List[Ueberweisung]] = None

    urheber: Optional[List[Urheber]] = None
