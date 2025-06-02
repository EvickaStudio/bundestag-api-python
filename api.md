# Vorgang

Types:

```python
from bundestag_api.types import ListResponseBase, Vorgang, VorgangListResponse
```

Methods:

- <code title="get /vorgang/{id}">client.vorgang.<a href="./src/bundestag_api/resources/vorgang.py">retrieve</a>(id, \*\*<a href="src/bundestag_api/types/vorgang_retrieve_params.py">params</a>) -> <a href="./src/bundestag_api/types/vorgang.py">Vorgang</a></code>
- <code title="get /vorgang">client.vorgang.<a href="./src/bundestag_api/resources/vorgang.py">list</a>(\*\*<a href="src/bundestag_api/types/vorgang_list_params.py">params</a>) -> <a href="./src/bundestag_api/types/vorgang_list_response.py">VorgangListResponse</a></code>

# Vorgangsposition

Types:

```python
from bundestag_api.types import (
    Fundstelle,
    Quadrant,
    Ressort,
    Urheber,
    Vorgangsposition,
    Vorgangspositionbezug,
    Zuordnung,
    VorgangspositionListResponse,
)
```

Methods:

- <code title="get /vorgangsposition/{id}">client.vorgangsposition.<a href="./src/bundestag_api/resources/vorgangsposition.py">retrieve</a>(id, \*\*<a href="src/bundestag_api/types/vorgangsposition_retrieve_params.py">params</a>) -> <a href="./src/bundestag_api/types/vorgangsposition.py">Vorgangsposition</a></code>
- <code title="get /vorgangsposition">client.vorgangsposition.<a href="./src/bundestag_api/resources/vorgangsposition.py">list</a>(\*\*<a href="src/bundestag_api/types/vorgangsposition_list_params.py">params</a>) -> <a href="./src/bundestag_api/types/vorgangsposition_list_response.py">VorgangspositionListResponse</a></code>

# Drucksache

Types:

```python
from bundestag_api.types import Drucksache, Vorgangsbezug, DrucksacheListResponse
```

Methods:

- <code title="get /drucksache/{id}">client.drucksache.<a href="./src/bundestag_api/resources/drucksache.py">retrieve</a>(id, \*\*<a href="src/bundestag_api/types/drucksache_retrieve_params.py">params</a>) -> <a href="./src/bundestag_api/types/drucksache.py">Drucksache</a></code>
- <code title="get /drucksache">client.drucksache.<a href="./src/bundestag_api/resources/drucksache.py">list</a>(\*\*<a href="src/bundestag_api/types/drucksache_list_params.py">params</a>) -> <a href="./src/bundestag_api/types/drucksache_list_response.py">DrucksacheListResponse</a></code>

# DrucksacheText

Types:

```python
from bundestag_api.types import DokumentTextBase, DrucksacheText, DrucksacheTextListResponse
```

Methods:

- <code title="get /drucksache-text/{id}">client.drucksache_text.<a href="./src/bundestag_api/resources/drucksache_text.py">retrieve</a>(id, \*\*<a href="src/bundestag_api/types/drucksache_text_retrieve_params.py">params</a>) -> <a href="./src/bundestag_api/types/drucksache_text.py">DrucksacheText</a></code>
- <code title="get /drucksache-text">client.drucksache_text.<a href="./src/bundestag_api/resources/drucksache_text.py">list</a>(\*\*<a href="src/bundestag_api/types/drucksache_text_list_params.py">params</a>) -> <a href="./src/bundestag_api/types/drucksache_text_list_response.py">DrucksacheTextListResponse</a></code>

# Plenarprotokoll

Types:

```python
from bundestag_api.types import Plenarprotokoll, PlenarprotokollListResponse
```

Methods:

- <code title="get /plenarprotokoll/{id}">client.plenarprotokoll.<a href="./src/bundestag_api/resources/plenarprotokoll.py">retrieve</a>(id, \*\*<a href="src/bundestag_api/types/plenarprotokoll_retrieve_params.py">params</a>) -> <a href="./src/bundestag_api/types/plenarprotokoll.py">Plenarprotokoll</a></code>
- <code title="get /plenarprotokoll">client.plenarprotokoll.<a href="./src/bundestag_api/resources/plenarprotokoll.py">list</a>(\*\*<a href="src/bundestag_api/types/plenarprotokoll_list_params.py">params</a>) -> <a href="./src/bundestag_api/types/plenarprotokoll_list_response.py">PlenarprotokollListResponse</a></code>

# PlenarprotokollText

Types:

```python
from bundestag_api.types import PlenarprotokollText, PlenarprotokollTextListResponse
```

Methods:

- <code title="get /plenarprotokoll-text/{id}">client.plenarprotokoll_text.<a href="./src/bundestag_api/resources/plenarprotokoll_text.py">retrieve</a>(id, \*\*<a href="src/bundestag_api/types/plenarprotokoll_text_retrieve_params.py">params</a>) -> <a href="./src/bundestag_api/types/plenarprotokoll_text.py">PlenarprotokollText</a></code>
- <code title="get /plenarprotokoll-text">client.plenarprotokoll_text.<a href="./src/bundestag_api/resources/plenarprotokoll_text.py">list</a>(\*\*<a href="src/bundestag_api/types/plenarprotokoll_text_list_params.py">params</a>) -> <a href="./src/bundestag_api/types/plenarprotokoll_text_list_response.py">PlenarprotokollTextListResponse</a></code>

# Aktivitaet

Types:

```python
from bundestag_api.types import Aktivitaet, Deskriptor, AktivitaetListResponse
```

Methods:

- <code title="get /aktivitaet/{id}">client.aktivitaet.<a href="./src/bundestag_api/resources/aktivitaet.py">retrieve</a>(id, \*\*<a href="src/bundestag_api/types/aktivitaet_retrieve_params.py">params</a>) -> <a href="./src/bundestag_api/types/aktivitaet.py">Aktivitaet</a></code>
- <code title="get /aktivitaet">client.aktivitaet.<a href="./src/bundestag_api/resources/aktivitaet.py">list</a>(\*\*<a href="src/bundestag_api/types/aktivitaet_list_params.py">params</a>) -> <a href="./src/bundestag_api/types/aktivitaet_list_response.py">AktivitaetListResponse</a></code>

# Person

Types:

```python
from bundestag_api.types import Bundesland, Person, PersonListResponse
```

Methods:

- <code title="get /person/{id}">client.person.<a href="./src/bundestag_api/resources/person.py">retrieve</a>(id, \*\*<a href="src/bundestag_api/types/person_retrieve_params.py">params</a>) -> <a href="./src/bundestag_api/types/person.py">Person</a></code>
- <code title="get /person">client.person.<a href="./src/bundestag_api/resources/person.py">list</a>(\*\*<a href="src/bundestag_api/types/person_list_params.py">params</a>) -> <a href="./src/bundestag_api/types/person_list_response.py">PersonListResponse</a></code>
