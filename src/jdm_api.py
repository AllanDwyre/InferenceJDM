from __future__ import annotations
from requests_cache import CachedSession
from rich import print as rprint
from dataclasses import dataclass, asdict, field
from typing import List, Optional
from datetime import timedelta
import copy

@dataclass
class Term:
	id: int
	name: str
	type: int
	w: int
	c: Optional[int] = None
	level: Optional[float] = None
	infoid: Optional[int] = None
	creationdate: Optional[str] = None
	touchdate: Optional[str] = None

	api: Optional["JdmApi"] = field(default=None, repr=False, compare=False)

	def relation_with(self, other_term_name: str | Term, params: Optional["EndpointParams"] = None):
		if self.api is None:
			raise RuntimeError("API instance not set on Term object.")
		if isinstance(other_term_name, Term):
			other_term_name = other_term_name.name

		return self.api.fetch_relation_between(self.name, other_term_name, params)
	
	def get_relations(self, inverted=False, params: Optional["EndpointParams"] = None):
		if self.api is None:
			raise RuntimeError("API instance not set on Term object.")
		return self.api.fetch_relation(self.name, inverted, params)

@dataclass
class EndpointParams:
	types_ids: Optional[List[int]] = None
	not_types_ids: Optional[List[int]] = None
	min_weight: Optional[int] = None
	max_weight: Optional[int] = None
	relation_fields: Optional[List[str]] = None
	node_fields: Optional[List[str]] = None
	limit: Optional[int] = 0
	without_nodes: bool = False

	def copy(self) -> EndpointParams:
		return copy.deepcopy(self)

	def to_query_params(self):
		def serialize(value):
			if isinstance(value, list):
				return ",".join(map(str, value))
			return value

		return {
			key: serialize(value)
			for key, value in asdict(self).items()
			if value is not None
		}

@dataclass
class RelationResult:
	nodes: List[Term]
	relations: List[Relation]

	def _enrich_relations(self, relation_types: dict[int, RelationType]):
		node_map = {term.id: term for term in self.nodes}
		for rel in self.relations:
			rel.sujet = node_map[rel.node1]
			rel.objet = node_map[rel.node2]
			rel.relation_type = relation_types[rel.type]
			
	@staticmethod
	def from_dict(data: dict, api: JdmApi):
		nodes = [Term(**n, api=api) for n in data["nodes"]]
		relations = [Relation(**r) for r in data["relations"]]
		relation_result = RelationResult(nodes=nodes, relations=relations)
		relation_result._enrich_relations(api.relation_types)
		return relation_result
	
	def __str__(self):
		p = ""
		for rel in self.relations:
			p+= f"{rel.sujet.name} ({rel.relation_type.gpname}) {rel.objet.name} | {rel.w} \n"
		return p
	
@dataclass
class Relation:
	id: int
	node1: int
	node2: int
	type: int
	w: float

	sujet: Optional["Term"] = None
	objet: Optional["Term"] = None
	relation_type: Optional["RelationType"] = None

	def __str__(self):
		return f"{self.sujet.name} ({self.relation_type.gpname}) {self.objet.name} | {self.w}"

@dataclass
class RelationType:
	id: int
	name: str
	gpname: str
	help: str
	oppos: int
	posyes: str
	posno: str

class JdmApi:
	def __init__(self, base_url="https://jdm-api.demo.lirmm.fr/v0"):
		self._base_url = base_url
		self._session = CachedSession('database/jdm_api_cache', expire_after=timedelta(days=2))
		self.relation_types = self.fetch_relations_types()

	def _getEndpoint(self, endpoint: str):
		return f"{self._base_url}/{endpoint}"

	def _fetch(self, endpoint: str, params=None):
		return self._session.get(self._getEndpoint(endpoint), params=params)

	def get_relation_type_by_name(self, name: str) -> RelationType | None:
		"""
		Récupère l'identifiant d'un type de relation en le cherchant par son nom.
		"""
		for relation_type in self.relation_types.values():
			if relation_type.name == name or relation_type.gpname == name:
				return relation_type
		return None


	def fetch_term_by_name(self, term : str) -> Term | None:
		"""
		Récupère les informations d'un terme (mot) en le cherchant par son nom.
		"""
		response = self._fetch(f"node_by_name/{term}")
		if response.status_code == 200:
			return Term(**response.json(), api=self)
		else:
			print(f"Erreur lors de la récupération du terme '{term}' (code {response.status_code})")
			response.raise_for_status()

	def fetch_term_by_id(self, term_id) -> Term | None:
		"""
		Récupère les informations d'un terme (mot) en le cherchant par son identifiant numérique.
		"""
		response = self._fetch(f"node_by_id/{term_id}")
		if response.status_code == 200:
			return Term(**response.json(), api=self)
		else:
			print(f"Erreur lors de la récupération du terme '{term_id}' (code {response.status_code})")
			response.raise_for_status()

	def fetch_relation_between(self, sujet, objet, params: Optional[EndpointParams] = None):
		"""
		Fetch relations between two specific terms (sujet -> objet).
		Accepts EndpointParams for filtering.
		"""
		endpoint = f"relations/from/{sujet}/to/{objet}"
		query_params = params.to_query_params() if params else {}

		response = self._fetch(endpoint, params=query_params)
		if response.status_code == 200:
			return RelationResult.from_dict(response.json(), api=self)
		else:
			print(f"Erreur lors de la récupération des relations '{sujet}' & '{objet}' (code {response.status_code})")
			response.raise_for_status()

	def fetch_relation(self, term, inverted=False, params: Optional[EndpointParams] = None):
		"""
		Récupère les relations d'un terme donné.
		Si `inverted` est False, récupère les relations sortantes (to),
		sinon récupère les relations entrantes (from).
		Prend en option des filtres via `EndpointParams`.
		"""
		endpoint = f"relations/to/{term}" if inverted else f"relations/from/{term}"
		query_params = params.to_query_params() if params else {}

		response = self._fetch(endpoint, params=query_params)
		if response.status_code == 200:
			return RelationResult.from_dict(response.json(), api=self)
		else:
			print(f"Erreur lors de la récupération des relations de '{term}' (code {response.status_code})")
			response.raise_for_status()

	def fetch_relations_types(self):
		"""
		Récupère la liste des types de relations disponibles dans l'API JDM.
		Retourne une liste d'objets `RelationType`.
		"""
		response = self._fetch("relations_types")
		if response.status_code == 200:
			raw_data = response.json()
			return {item["id"] :  RelationType(
				id=item["id"],
				name=item["name"],
				gpname=item["gpname"],
				help=item["help"],
				oppos=item["oppos"],
				posyes=item["posyes"],
				posno=item["posno"]
			) for item in raw_data}
		else:
			response.raise_for_status()

