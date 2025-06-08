from src.jdm_api import EndpointParams, JdmApi, Term
from rich import print as rprint
import src.logger as log

import asyncio
import aiohttp
from typing import List

from statistics import harmonic_mean
from dataclasses import dataclass

@dataclass
class Inference:
	sujet	: str
	objet	: str
	gen		: str

	weight1 : int
	weight2 : int

	t 		: str # type d'inférence : isa | hypo | 
	rel		: str # type de relation : has_part | lieu | ... 
	score	: float = 0.0



class RelationInferer:
	def __init__(self, api:JdmApi, limit=10, max_treads_per_type=4, max_thread_per_branch=10,
			  inferenceLogger = log.InferenceLogger()):
		"""
        Initialise un inféreur de relations basé sur une trame (sujet, relation, objet) en s'appuyant sur l'API JDM.

        Ce module permet de découvrir de nouvelles relations sémantiques à partir d'une relation de base, en explorant
        les connaissances disponibles via l'API JeuxDeMots (JDM). La recherche est parallélisée pour améliorer l'efficacité.

        Paramètres :
        - sujet (str) : Terme de départ de la relation.
        - relation (str) : Type de relation (prédicat) à explorer.
        - objet (str) : Terme d'arrivée de la relation.
        - api (JdmApi) : Instance de l'API JDM utilisée pour interroger le graphe lexical.
        - limit (int) : Nombre maximal de résultats à retourner (par défaut : 10).
        - max_treads_per_type (int) : Nombre maximal de threads à lancer par type de relation (par défaut : 4).
        - max_thread_per_branch (int) : Nombre maximal de threads pour explorer chaque branche de la recherche (par défaut : 10).
        """

		self.api = api
		self.limit = limit
		self.default_params = EndpointParams(min_weight=1, limit=100)
		self.logger = inferenceLogger

	def normalize_and_score(self, inferences: list[Inference]):
		all_weights1 = [inf.weight1 for inf in inferences]
		all_weights2 = [inf.weight2 for inf in inferences]

		max_w1 = max(all_weights1)
		max_w2 = max(all_weights2)

		for inf in inferences:
			norm_w1 = inf.weight1 / max_w1 if max_w1 else 0
			norm_w2 = inf.weight2 / max_w2 if max_w2 else 0

			# Moyenne harmonique (évite division par 0)
			if norm_w1 > 0 and norm_w2 > 0:
				inf.score = harmonic_mean([norm_w1, norm_w2])
			else:
				inf.score = 0.0


	async def inference_by_generalization(self, sujet: Term, objet: Term, final_rel_id: int):
		params = self.default_params.copy()
		params.types_ids = [self.api.get_relation_type_by_name("r_isa").id]

		r_isa_rel = objet.get_relations(params=params).relations
		r_isa_rel = sorted(r_isa_rel, key=lambda r: r.w, reverse=True)

		params = self.default_params.copy()
		params.types_ids = [final_rel_id]
		
		inferences: list[Inference] = []
		for rel in r_isa_rel:
			final_rel = sujet.relation_with(rel.objet, params)
			if final_rel.relations :
				inferred = Inference(
					sujet=sujet.name,
					gen=rel.objet.name,
					objet=objet.name,
					weight1=rel.w,
					weight2=final_rel.relations[0].w,
					t="isa",
					rel=final_rel.relations[0].relation_type.name,
				)
				inferences.append(inferred)
		
		return inferences

	def inference_by_specialization(self, sujet: Term, objet: Term, final_rel_id: int):
		params = self.default_params.copy()
		params.types_ids = [self.api.get_relation_type_by_name("r_hypo").id]

		r_hypo_rel = sujet.get_relations(params=params).relations
		r_hypo_rel = sorted(r_hypo_rel, key=lambda r: r.w, reverse=True)
		
		params = self.default_params.copy()
		params.types_ids = [final_rel_id]
		
		inferences: list[Inference] = []
		for rel in r_hypo_rel:
			final_rel = rel.objet.relation_with(objet, params)
			if final_rel.relations :
				inferred = Inference(
					sujet=sujet.name,
					gen=rel.objet.name,
					objet=objet.name,
					weight1=rel.w,
					weight2=final_rel.relations[0].w,
					t="hypo",
					rel=final_rel.relations[0].relation_type.name,
				)
				inferences.append(inferred)
		
		return inferences

	def inference_by_synonyme(self, sujet: Term, objet: Term, final_rel_id: int):
		params = self.default_params.copy()
		params.types_ids = [self.api.get_relation_type_by_name("r_syn").id]

		r_hypo_rel = sujet.get_relations(params=params).relations
		r_hypo_rel = sorted(r_hypo_rel, key=lambda r: r.w, reverse=True)
		
		params = self.default_params.copy()
		params.types_ids = [final_rel_id]
		
		inferences: list[Inference] = []
		for rel in r_hypo_rel:
			final_rel = rel.objet.relation_with(objet, params)
			if final_rel.relations :
				inferred = Inference(
					sujet=sujet.name,
					gen=rel.objet.name,
					objet=objet.name,
					weight1=rel.w,
					weight2=final_rel.relations[0].w,
					t="syn",
					rel=final_rel.relations[0].relation_type.name,
				)
				inferences.append(inferred)
		
		return inferences

	def inference_by_lieu(self, sujet: Term, objet: Term, final_rel_id: int):
		params = self.default_params.copy()
		params.types_ids = [self.api.get_relation_type_by_name("r_lieu").id]

		r_hypo_rel = sujet.get_relations(params=params).relations
		r_hypo_rel = sorted(r_hypo_rel, key=lambda r: r.w, reverse=True)
		
		params = self.default_params.copy()
		params.types_ids = [final_rel_id]
		
		inferences: list[Inference] = []
		for rel in r_hypo_rel:
			final_rel = rel.objet.relation_with(objet, params)
			if final_rel.relations :
				inferred = Inference(
					sujet=sujet.name,
					gen=rel.objet.name,
					objet=objet.name,
					weight1=rel.w,
					weight2=final_rel.relations[0].w,
					t="syn",
					rel=final_rel.relations[0].relation_type.name,
				)
				inferences.append(inferred)
		
		return inferences
	
	def inference_by_holo(self, sujet: Term, objet: Term, final_rel_id: int):
		params = self.default_params.copy()
		params.types_ids = [self.api.get_relation_type_by_name("r_holo").id]

		r_hypo_rel = sujet.get_relations(params=params).relations
		r_hypo_rel = sorted(r_hypo_rel, key=lambda r: r.w, reverse=True)
		
		params = self.default_params.copy()
		params.types_ids = [final_rel_id]
		
		inferences: list[Inference] = []
		for rel in r_hypo_rel:
			final_rel = rel.objet.relation_with(objet, params)
			if final_rel.relations :
				inferred = Inference(
					sujet=sujet.name,
					gen=rel.objet.name,
					objet=objet.name,
					weight1=rel.w,
					weight2=final_rel.relations[0].w,
					t="syn",
					rel=final_rel.relations[0].relation_type.name,
				)
				inferences.append(inferred)
		
		return inferences
	
	def inference_by_has_part(self, sujet: Term, objet: Term, final_rel_id: int):
		params = self.default_params.copy()
		params.types_ids = [self.api.get_relation_type_by_name("r_has_part").id]

		r_hypo_rel = sujet.get_relations(params=params).relations
		r_hypo_rel = sorted(r_hypo_rel, key=lambda r: r.w, reverse=True)
		
		params = self.default_params.copy()
		params.types_ids = [final_rel_id]
		
		inferences: list[Inference] = []
		for rel in r_hypo_rel:
			final_rel = rel.objet.relation_with(objet, params)
			if final_rel.relations :
				inferred = Inference(
					sujet=sujet.name,
					gen=rel.objet.name,
					objet=objet.name,
					weight1=rel.w,
					weight2=final_rel.relations[0].w,
					t="syn",
					rel=final_rel.relations[0].relation_type.name,
				)
				inferences.append(inferred)
		
		return inferences

	
	def run(self, sujet_name:str, relation_name:str, objet_name:str) -> None:
		"""Run the inference process."""
		try:
			sujet, objet = (self.api.fetch_term_by_name(sujet_name), self.api.fetch_term_by_name(objet_name))
			rel_id = self.api.get_relation_type_by_name(relation_name).id

		except Exception as e:
			return
		
		inferences = self.inference_by_generalization(sujet, objet, rel_id)
		inferences.extend(self.inference_by_specialization(sujet, objet, rel_id))
		inferences.extend(self.inference_by_has_part(sujet, objet, rel_id))
		inferences.extend(self.inference_by_lieu(sujet, objet, rel_id))
		inferences.extend(self.inference_by_holo(sujet, objet, rel_id))
		inferences.extend(self.inference_by_synonyme(sujet, objet, rel_id))

		if len(inferences) == 0:
			self.logger.render_inferences(inferences)
			return

		self.normalize_and_score(inferences)
		inferences = sorted(inferences, key=lambda r: r.score, reverse=True)[:self.limit]
		
		self.logger.render_inferences(inferences)
		
		# TODO : [ ] Multi-thread pour chaque type
		# TODO : [ ] Multi-thread pour chaque chemin par type
		# TODO : [ ] Prendre en compte les annotations (pour que ce soit des modifier de notes)
		# TODO : [ ] Faire les 5 inférences (isa, hypo, ...)
		# TODO : [ ] Faire un meilleur formatage
		# TODO : [x] 2 type de logger un pour le bot, l'autre pour le cli

		# transitive direct, indirect, subjective, inductive
		# bot discord,
		# annotation : 
