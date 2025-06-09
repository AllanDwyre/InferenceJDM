from rich.console import Console
from rich.text import Text


class InferenceLogger:
	def __init__(self):
		self.console = Console()

	def format_title(self, text: str, width: int = 110):
		return f"[bold]{text:^{width}}[/bold]"

	def _render_no_result(self):
		line = Text()
		# Numéro
		line.append(f"{'1':>3}. ", style="dim")
		# Emote + Non
		line.append("➤  non", style="bold red")
		self.console.print(line)

	def _render_single_inference(self, idx, inference):
		arrow = "➝ "
		# Texte de la ligne
		line = Text()

		# Numéro
		line.append(f"{idx:>3}. ", style="dim")

		# Emote + Oui
		line.append("➤  oui", style="bold green")
		line.append(" | ")

		# Explication : sujet ➝ gen ; gen ➝ obj
		size = max(len(inference.sujet),len(inference.objet))
		if inference.t in {"isa",""}: # cas spécial
			term1 = f"{inference.objet:<{size}}"
			term2 = f"{inference.sujet:<{size}}"
		else:
			term1 = f"{inference.sujet:<{size}}"
			term2 = f"{inference.objet:<{size}}"
		
		middle_rel = inference.t if (inference.t != "transitivity") else inference.rel

		line.append(term1, style="bold magenta")
		line.append(f" {middle_rel:<5}", style="italic dim")
		line.append(f" {arrow} ")
		line.append(f"{inference.gen:<45}", style="bold cyan")

		line.append(f"{inference.gen:<45}", style="bold cyan")
		line.append(f" {inference.rel}", style="italic dim")
		line.append(f" {arrow} ")
		line.append(term2, style="bold yellow")
		# Score
		line.append(" | ")

		score_style = (
			"bold green" if inference.score >= .7 else
			"yellow" if inference.score >= .5 else
			"red"
		)
		line.append(f"{inference.score:<.2f}", style=score_style)

		# Affichage
		self.console.print(line)

	def render_inferences(self, inferences):
		if len(inferences) == 0:
			self._render_no_result()
			return
		
		for idx, inferred in enumerate(inferences, 1):
			self._render_single_inference(idx, inferred)

class InferenceLoggerBot(InferenceLogger):
	def __init__(self, context, verbose = False):
		if(verbose):
			super().__init__()
		self.verbose = verbose
		self.context = context
		self.messages = []

	def _render_no_result(self):
		"""Override pour Discord"""
		if(self.verbose):
			super()._render_no_result()
		self.messages.append("```\n1. ➤ non\n```")

	def _render_single_inference(self, idx, inference):
		"""Override pour Discord avec formatage markdown"""
		if(self.verbose):
			super()._render_single_inference(idx, inference)

		score_emoji = "🟢" if inference.score >= .7 else "🟡" if inference.score >= .5 else "🔴"
		arrow = "➝ "

		size = max(len(inference.sujet),len(inference.objet))
		if inference.t in {"isa",""}: # cas spécial
			term1 = f"{inference.objet:<{size}}"
			term2 = f"{inference.sujet:<{size}}"
		else:
			term1 = f"{inference.sujet:<{size}}"
			term2 = f"{inference.objet:<{size}}"
		
		middle_rel = inference.t if (inference.t != "transitivity") else inference.rel

		message = (
			f"```\n"
			f"{idx:>3}. ✅ oui | "
			f"{term1} {middle_rel:<40} {arrow} "
			f"{inference.gen:<40} {inference.rel} {arrow} "
			f"{term2} | {score_emoji} {inference.score:<.2f}\n"
			f"```"
		)

		self.messages.append(message)

	async def send_all(self):
		"""Envoie tous les messages Discord accumulés"""
		if not self.messages:
			return
			
		combined = "\n".join(self.messages)
		if len(combined) < 2000:  # Limite de caractère Discord
			await self.context.send(combined)
		else:
			for msg in self.messages:
				await self.context.send(msg)