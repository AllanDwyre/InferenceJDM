from rich import print as rprint
from src.jdm_api import JdmApi, RelationResult, Term, Relation, TermNotFoundError
from src.inference import RelationInferer
import src.logger as log
import re
import asyncio

from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import shlex
import argparse

import time

# ----------------- INIT BOT -----------------------
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)


# ------------------- UTILS ------------------------
def parse_input(sentence: str) -> tuple[str, str, str] | None:
	"""Parse input sentence into word1, relation, and word2."""
	match = re.match(r"(.+?)\s+(r_\S+)\s+(.+)", sentence)
	if match:
		return match.groups()
	return None

# ------------------- CLI ------------------------

async def main_console() -> None:
	async with JdmApi() as api:
		inferer = RelationInferer(api=api)
		while(True):
			sentence = input("Enter a sentence (word1 r_relation word2): ").strip() or "pizza r_has_part mozza"
			parsed_sentence = parse_input(sentence)

			if not parsed_sentence:
				print("Invalid input format. Please use 'word1 r_relation word2'.")
				continue
			
			sujet, rel, objet = parsed_sentence

			rprint(f"[bold blue]Parsed Sentence:[/bold blue] {sujet} {rel} {objet}")

			# Check if the relation is valid
			rel_type = api.get_relation_type_by_name(rel)
			if not rel_type:
				rprint(f"[red]Relation '{rel}' not found in the API.[/red]")
				continue

			start = time.time()
			await inferer.run(sujet, rel, objet)
			print(f"Temps d'exécution : {time.time() - start:.4f} secondes")


# ------------------- BOT FUNC ------------------------

def main_bot() -> None:
	load_dotenv()
	
	TOKEN = os.getenv("DISCORD_TOKEN")
	bot.run(TOKEN)
	

@bot.command()
async def inference(ctx, sujet, relation, objet, *args):
	"""
    Commande pour faire une inférence de relation.
    Je laisse python gérer le parsing de sujet, relation, objet, et je laisse argparse de gérer les arguments en plus
    Usage:
        !inference chat r_isa animal
        !inference chat r_isa animal --limit 15
        !inference pizza r_has_part mozza --limit 5
    """
	if not sujet and not relation and not objet:
		await ctx.send("Usage: `!inference <sujet> <relation> <objet> [--limit N] `\nExemple: `!inference chat r_isa animal --limit 10`")
		return
	
	rprint(f"[bold blue]Parsed Sentence:[/bold blue] {sujet} {relation} {objet}")

	parser = argparse.ArgumentParser()
	parser.add_argument("--limit", type=int, default=10, help='Limite de résultats (défaut: 10)')

	try:
		async with JdmApi() as api:
			args = parser.parse_args(shlex.split(" ".join(args)))
			await ctx.send(f"## Inférence de {sujet} {relation} {objet} avec limite {args.limit}")

			rel_type = api.get_relation_type_by_name(relation)
			if not rel_type:
				rprint(f"[red]Relation '{relation}' not found in the API.[/red]")
				await ctx.send(f"Relation '{relation}' not found in the API.")
				return

			start = time.time()

			logger = log.InferenceLoggerBot(context=ctx, verbose=True)
			await RelationInferer(
				limit=args.limit,
				api=api,
				inferenceLogger= logger
			).run(sujet, relation, objet)

			await logger.send_all()

			print(f"Temps d'exécution : {time.time() - start:.4f} secondes")
	except TermNotFoundError as e:
				if e.status_code == 500:
					await ctx.send(f"❌ **Erreur serveur**: Le terme `{e.term_name}` a causé une erreur interne (500). Il pourrait ne pas exister ou contenir des caractères spéciaux.")
				else:
					await ctx.send(f"❌ **Terme non trouvé**: `{e.term_name}` n'existe pas dans la base de données.")
	except SystemExit:
		await ctx.send("Erreur de syntaxe dans la commande.")


def main() -> None:

	parser = argparse.ArgumentParser()

	parser = argparse.ArgumentParser()
	parser.add_argument("-B", "--bot", action="store_true", help="Lancer le bot Discord")
	
	args = parser.parse_args()

	if args.bot:
		main_bot()
	else :
		asyncio.run(main_console())


if __name__ == "__main__":
	main()