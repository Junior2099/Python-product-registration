from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'descricao', 'estoque']
        
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }