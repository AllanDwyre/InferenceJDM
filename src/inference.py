from src.jdm_api import EndpointParams, JdmApi, Term
from rich import print as rprint

import src.logger as log
import logging
import traceback

import asyncio

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
	score	: float = 0.0,

	annotation_weight1 : float = 1.0,
	annotation_weight2 : float = 1.0,



class RelationInferer:
	def __init__(self, api:JdmApi, limit=10, inferenceLogger = log.InferenceLogger()):
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

			annotation_weight = inf.annotation_weight1 * inf.annotation_weight2
			inf.score *= annotation_weight

	async def inference_by_generalization(self, sujet: Term, objet: Term, final_rel_id: int):
		params = self.default_params.copy()
		params.types_ids = [self.api.get_relation_type_by_name("r_isa").id]

		r_isa_rel = await objet.get_relations(params=params)
		r_isa_rel = sorted(r_isa_rel.relations, key=lambda r: r.w, reverse=True)

		params = self.default_params.copy()
		params.types_ids = [final_rel_id]
		

		async def get_final_rel(rel):
			await rel.get_annotation(self.api)
			rel_annotation_weight = rel.get_annotation_weight()

			result = await sujet.relation_with(rel.objet, params)
			if result.relations:
				final_relation = result.relations[0]
				await final_relation.get_annotation(self.api)
				final_annotation_weight = final_relation.get_annotation_weight()
		
				return Inference(
					sujet=sujet.name,
					gen=rel.objet.name,
					objet=objet.name,
					weight1=rel.w,
					weight2=final_relation.w,
					t="isa",
					rel=final_relation.relation_type.name,

					annotation_weight1=rel_annotation_weight,
					annotation_weight2=final_annotation_weight,
				)
			return None

		tasks = [get_final_rel(rel) for rel in r_isa_rel]
		results = await asyncio.gather(*tasks, return_exceptions=True)
		
		inferences = [r for r in results if r is not None and not isinstance(r, Exception)]
		
		return inferences

	async def inference_by_specialization(self, sujet: Term, objet: Term, final_rel_id: int):
		params = self.default_params.copy()
		params.types_ids = [self.api.get_relation_type_by_name("r_hypo").id]

		r_hypo_rel = await sujet.get_relations(params=params)
		r_hypo_rel = sorted(r_hypo_rel.relations, key=lambda r: r.w, reverse=True)
		
		params = self.default_params.copy()
		params.types_ids = [final_rel_id]
		
		async def get_final_rel(rel):
			await rel.get_annotation(self.api)
			rel_annotation_weight = rel.get_annotation_weight()

			result = await rel.objet.relation_with(objet, params)
			if result.relations:
				final_relation = result.relations[0]
				await final_relation.get_annotation(self.api)
				final_annotation_weight = final_relation.get_annotation_weight()

				return Inference(
					sujet=sujet.name,
					gen=rel.objet.name,
					objet=objet.name,
					weight1=rel.w,
					weight2=final_relation.w,
					t="hypo",
					rel=final_relation.relation_type.name,

					annotation_weight1=rel_annotation_weight,
					annotation_weight2=final_annotation_weight,
				)
			return None

		tasks = [get_final_rel(rel) for rel in r_hypo_rel]
		results = await asyncio.gather(*tasks, return_exceptions=True)
		
		inferences = [r for r in results if r is not None and not isinstance(r, Exception)]
		
		return inferences

	async def inference_by_transitivity(self, sujet: Term, objet: Term, final_rel_id: int):
		params = self.default_params.copy()
		params.types_ids = [final_rel_id]

		r_trans_rel = await sujet.get_relations(params=params)
		r_trans_rel = sorted(r_trans_rel.relations, key=lambda r: r.w, reverse=True)
		
		async def get_final_rel(rel):
			await rel.get_annotation(self.api)
			rel_annotation_weight = rel.get_annotation_weight()

			result = await rel.objet.relation_with(objet, params)
			if result.relations:
				final_relation = result.relations[0]
				await final_relation.get_annotation(self.api)
				final_annotation_weight = final_relation.get_annotation_weight()
				
				return Inference(
					sujet=sujet.name,
					gen=rel.objet.name,
					objet=objet.name,
					weight1=rel.w,
					weight2=final_relation.w,
					t="transitivity",
					rel=final_relation.relation_type.name,

					annotation_weight1=rel_annotation_weight,
					annotation_weight2=final_annotation_weight,
				)
			return None

		tasks = [get_final_rel(rel) for rel in r_trans_rel]
		results = await asyncio.gather(*tasks, return_exceptions=True)
		
		inferences = [r for r in results if r is not None and not isinstance(r, Exception)]
		
		return inferences
	
	async def inference_by_synonymy(self, sujet: Term, objet: Term, final_rel_id: int):
		params = self.default_params.copy()
		params.types_ids = [self.api.get_relation_type_by_name("r_syn").id]

		r_syn_rel = await sujet.get_relations(params=params)
		r_syn_rel = sorted(r_syn_rel.relations, key=lambda r: r.w, reverse=True)
		
		params = self.default_params.copy()
		params.types_ids = [final_rel_id]
		
		async def get_final_rel(middle_rel):
			await middle_rel.get_annotation(self.api)
			rel_annotation_weight = middle_rel.get_annotation_weight()

			result = await middle_rel.objet.relation_with(objet, params)
			if result.relations:
				final_relation = result.relations[0]
				await final_relation.get_annotation(self.api)
				final_annotation_weight = final_relation.get_annotation_weight()

				return Inference(
					sujet=sujet.name,
					gen=middle_rel.objet.name,
					objet=objet.name,
					weight1=middle_rel.w,
					weight2=final_relation.w,
					t="syn",
					rel=final_relation.relation_type.name,

					annotation_weight1=rel_annotation_weight,
					annotation_weight2=final_annotation_weight,
				)
			return None

		tasks = [get_final_rel(rel) for rel in r_syn_rel]
		results = await asyncio.gather(*tasks, return_exceptions=True)
		
		inferences = [r for r in results if r is not None and not isinstance(r, Exception)]
		
		return inferences

	async def run_all_inferences(self, sujet, objet, rel_id):
		sujet.api = self.api
		objet.api = self.api

		tasks = [
			self.inference_by_generalization(sujet, objet, rel_id),
			self.inference_by_specialization(sujet, objet, rel_id),
			self.inference_by_transitivity(sujet, objet, rel_id),
			self.inference_by_synonymy(sujet, objet, rel_id),
		]
		
		results = await asyncio.gather(*tasks, return_exceptions=True)
		
		inferences = []
		for result in results:
			if isinstance(result, Exception):
				print(f"Erreur: {result}")
			else:
				inferences.extend(result)

		return inferences
	
	async def run(self, sujet_name:str, relation_name:str, objet_name:str) -> None:
		"""Run the inference process."""
		try:
			sujet, objet = (await self.api.fetch_term_by_name(sujet_name), await self.api.fetch_term_by_name(objet_name))
			rel_id = self.api.get_relation_type_by_name(relation_name).id

		except Exception as e:
			rprint(f"[red] Erreur lors de l'initialisation: {e}[/red]")
			raise e		
		inferences = await self.run_all_inferences(sujet, objet, rel_id)

		if len(inferences) == 0:
			self.logger.render_inferences(inferences)
			return

		self.normalize_and_score(inferences)
		inferences = sorted(inferences, key=lambda r: r.score, reverse=True)[:self.limit]
		
		self.logger.render_inferences(inferences)
	
		# TODO : [x] Multi-thread pour chaque type
		# TODO : [x] Multi-thread pour chaque chemin par type
		# TODO : [x] Prendre en compte les annotations (pour que ce soit des modifier de notes)
		# TODO : [x] Faire les 4 inférences (isa, hypo, transitivity, syn) 
		# TODO : [ ] Faire un meilleur formatage
		# TODO : [x] 2 type de logger un pour le bot, l'autre pour le cli
		# TODO : [x] Mettre sur github
