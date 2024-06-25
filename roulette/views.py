from django.shortcuts import render
from django.http import JsonResponse
from roulette.models import Agent, Map, Text, AgentSpecificText, MapSpecificText
from random import choice, randint
from django.db.models import Q
from .forms import RouletteForm

AGENT_TEXT_PERCENTAGE = 10
MAP_TEXT_PERCENTAGE = 10


def get_text(val_map=None, agents=[], attacking=False, defending=False):
    print(val_map, [agent.name_en for agent in agents], attacking, defending, sep="; ")
    
    texts = Text.objects.all()
    rand = randint(0, 100)
    
    if val_map and agents:
        if rand < AGENT_TEXT_PERCENTAGE:
            agent = choice(agents)
            texts = agent.agentspecifictext_set.all()
        elif rand < (AGENT_TEXT_PERCENTAGE + MAP_TEXT_PERCENTAGE):
            texts = val_map.mapspecifictext_set.all()
    elif val_map:
        if rand < MAP_TEXT_PERCENTAGE:
            texts = val_map.mapspecifictext_set.all()
    elif agents:
        if rand < AGENT_TEXT_PERCENTAGE:
            agent = choice(agents)
            texts = agent.agentspecifictext_set.all()
    
    if not attacking and not defending:
        texts = texts.filter(attacking=False, defending=False)
    else:
        texts = texts.filter(
            Q(attacking=attacking, defending=defending) | 
            Q(attacking=False, defending=False)
        )
    
    text = choice(texts)
    text_str = text.text
    
    if text.attacking:
        text_str = text_str.removeprefix("__attacking__ ")
    if text.defending:
        text_str = text_str.removeprefix("__defending__ ")
    if text.random_player:
        text_str = text_str.replace("__random_player__", choice(agents).name_en if agents else "A random player")
    
    return text_str


# Create your views here.
def index(request):
    if request.method == "POST":
        form = RouletteForm(request.POST)
        if form.is_valid():
            val_map = form.cleaned_data["mapfield"]
            agents = form.cleaned_data["agentfield"]
            if val_map == "default":
                val_map = None
            else:
                val_map = Map.objects.get(name_en=val_map)
            if agents:
                agents = [Agent.objects.get(name_en=agent) for agent in agents]
            attacking = "Attacking" in form.cleaned_data["sidefield"]
            defending = "Defending" in form.cleaned_data["sidefield"]
            return JsonResponse(
                {
                    "text": get_text(
                        val_map=val_map,
                        agents=agents,
                        attacking=attacking,
                        defending=defending,
                    )
                }
            )
    context = {}
    context["text"] = choice(
        Text.objects.filter(random_player=False, attacking=False, defending=False)
    )
    context["form"] = RouletteForm()
    if request.user_agent.is_mobile:
        return render(request, "roulette/mobile.html", context=context)
    return render(request, "roulette/index.html", context=context)
