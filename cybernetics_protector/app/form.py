from django import forms

from .models import Assign_Agent,CaseAssign_Agent

class Agent_AsignForm(forms.ModelForm):
    class Meta:
        model=Assign_Agent
        fields='__all__'

class CaseAssign_AgentForm(forms.ModelForm):
    class Meta:
        model=CaseAssign_Agent
        fields='__all__'


