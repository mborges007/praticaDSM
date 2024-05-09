from django import forms

class AgendaForm(forms.Form):
    nome = forms.CharField(max_length=150)
    telefone = forms.CharField(max_length=20)
    cpf = forms.CharField(max_length=30)  # Definindo o campo sem valor padrão

    def __init__(self, *args, **kwargs):
        super(AgendaForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].initial = ''  # Definindo o valor padrão para o campo cpf
