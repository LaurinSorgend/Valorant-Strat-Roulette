from django.shortcuts import render
from roulette.models import Agent, Map, Text, AgentSpecificText, MapSpecificText
from random import choice, randint
from itertools import chain

AGENT_TEXT_PERCENTAGE = 10
MAP_TEXT_PERCENTAGE = 10


def get_text(val_map=None, agents=[], attacking=False, defending=False):
    print(val_map, len(agents), attacking, defending, sep="; ")
    texts = Text.objects.all()
    if val_map and agents:
        rand = randint(0, 100)
        if rand < AGENT_TEXT_PERCENTAGE:
            agent = choice(agents)
            texts = agent.agentspecifictext_set.all()
        elif rand < (AGENT_TEXT_PERCENTAGE + MAP_TEXT_PERCENTAGE):
            texts = val_map.mapspecifictext_set.all()
    elif val_map:
        rand = randint(0, 100)
        if rand < AGENT_TEXT_PERCENTAGE:
            agent = choice(agents)
            texts = agent.agentspecifictext_set.all()
    elif agents:
        rand = randint(0, 100)
        if rand < AGENT_TEXT_PERCENTAGE:
            agent = choice(agents)
            texts = agent.agentspecifictext_set.all()
    if not attacking and not defending:
        texts = texts.filter(attacking=False, defending=False)
    else:
        # spec_list = list(texts.filter(attacking=attacking, defending=defending))
        # gene_list = list(texts.filter(attacking=False, defending=False))
        texts = list(
            chain(
                texts.filter(attacking=attacking, defending=defending),
                texts.filter(attacking=False, defending=False),
            )
        )
    text = choice(texts)
    text_str = text.text
    if text.attacking:
        text_str = text_str.removeprefix("__attacking__ ")
    if text.defending:
        text_str = text_str.removeprefix("__defending__ ")
    if text.random_player:
        if agents:
            text_str = text_str.replace("__random_player__", choice(agents).name_en)
        else:
            text_str = text_str.replace("__random_player__", "A random player")
    return text_str


# Create your views here.
def index(request):
    return render(
        request,
        "roulette/index.html",
        {"text": get_text(agents=list(Agent.objects.all()))},
    )