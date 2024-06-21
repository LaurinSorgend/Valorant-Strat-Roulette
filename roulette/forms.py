from django import forms
from .models import Agent, Map


# agent_names = [(agent.name_en, agent.name_en) for agent in Agent.objects.all()]
map_names = [("default", "Select a Map")] + [(val_map.name_en, val_map.name_en) for val_map in Map.objects.all()]
class RouletteForm(forms.Form):
    mapfield = forms.ChoiceField(
        choices=map_names,
        label="Select a Map",
        initial="default",
        widget=forms.Select(
            attrs={
                "class": ""
            }
        ),
    )
    # agentfield = forms.ChoiceField(
    #     choices=agent_names,
    #     label="",
    #     widget=forms.Select(
    #         attrs={
    #             "class": "mt-1 block w-full pl-3 pr-10 py-8 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
    #         }
    #     ),
    # )
