from django.core.management.base import BaseCommand, CommandError
import json
from roulette.models import Agent, Map, Text, AgentSpecificText, MapSpecificText
from frenly_goobers.settings import BASE_DIR


class Command(BaseCommand):
    help = "Loads data from json file into db"

    JSON_PATH = BASE_DIR / "texts.json"

    def handle(self, *args, **options):
        agents = list(Agent.objects.all())
        maps = list(Map.objects.all())
        with open(self.JSON_PATH, "r") as f:
            dic = json.load(f)
        for text in dic["generic"]:
            if not Text.objects.filter(text=text).exists():
                t = Text(text=text)
                if t.text.startswith("__attacking__"):
                    t.attacking = True
                if t.text.startswith("__defending__"):
                    t.defending = True
                if t.text.startswith("__random_player__"):
                    t.random_player = True
                t.save()
                self.stdout.write(
                    self.style.SUCCESS('Successfully added "%s" to database' % t.text)
                )
        for agent in agents:
            for agent_text in dic["agents"][agent.name_en]:
                if not AgentSpecificText.objects.filter(
                    agent=agent, text=agent_text
                ).exists():
                    ast = AgentSpecificText(text=agent_text, agent=agent)
                    if ast.text.startswith("__attacking__"):
                        ast.attacking = True
                    if ast.text.startswith("__defending__"):
                        ast.defending = True
                    if ast.text.startswith("__random_player__"):
                        ast.random_player = True
                    ast.save()
                    self.stdout.write(
                        self.style.SUCCESS('Successfully added "%s" to database' % ast.text)
                    )
        for val_map in maps:
            for map_text in dic["maps"][val_map.name_en]:
                if not MapSpecificText.objects.filter(
                    map=val_map, text=map_text
                ).exists():
                    mst = MapSpecificText(text=map_text, map=val_map)
                    if mst.text.startswith("__attacking__"):
                        mst.attacking = True
                    if mst.text.startswith("__defending__"):
                        mst.defending = True
                    if mst.text.startswith("__random_player__"):
                        mst.random_player = True
                    mst.save()
                    self.stdout.write(
                        self.style.SUCCESS('Successfully added "%s" to database' % mst.text)
                    )
