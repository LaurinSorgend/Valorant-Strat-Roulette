from django.core.management.base import BaseCommand, CommandError
import json
from roulette.models import Agent, Map, Text
from frenly_goobers.settings import BASE_DIR


class Command(BaseCommand):
    help = "Generate a json file with all current Roulette Texts"

    TMP_TEXT = "This is a placeholder for a text for __blank__."
    JSON_PATH = BASE_DIR / "texts.json"

    def handle(self, *args, **options):
        agents = list(Agent.objects.all())
        maps = list(Map.objects.all())
        texts = list(Text.objects.all())
        dic = {"generic": [], "agents": {}, "maps": {}}
        if not len(texts) == 0:
            for text in texts:
                dic["generic"].append(text.text)
        else:
            dic["generic"].append(self.TMP_TEXT.replace("__blank__", "a generic Text"))
        for agent in agents:
            agent_texts = agent.agentspecifictext_set.all()
            if not len(agent_texts) == 0:
                dic["agents"][agent.name_en] = []
                for agent_text in agent_texts:
                    dic["agents"][agent.name_en].append(agent_text.text)
            else:
                dic["agents"][agent.name_en] = [self.TMP_TEXT.replace("__blank__", agent.name_en)]
        for val_map in maps:
            map_texts = val_map.mapspecifictext_set.all()
            if not len(map_texts) == 0:
                dic["maps"][val_map.name_en] = []
                for map_text in map_texts:
                    dic["maps"][val_map.name_en].append(map_text.text)
            else:
                dic["maps"][val_map.name_en] = [self.TMP_TEXT.replace("__blank__", val_map.name_en)]
        with open(self.JSON_PATH, 'w') as f:
            json.dump(dic, f, indent=4)