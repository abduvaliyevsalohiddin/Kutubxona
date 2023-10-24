from django import forms

from .models import *

class TalabaForm(forms.Form):
    ism = forms.CharField(label="Ism")
    kurs = forms.IntegerField(label="Kurs", max_value=7, min_value=1)
    kitob_soni = forms.IntegerField(label="Kitoblar soni")


class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = "__all__" #["ism", "jins", ..... ]

    # ism = forms.CharField(label="Ism")
    # jins = forms.CharField(label="Jins", max_length=5, min_length=1)
    # tugulgan_kun = forms.DateField(label="Tugulgan kun")
    # kitoblar_soni = forms.IntegerField(label="Kitoblar soni")
    # tirik = forms.BooleanField(label="Tirik")

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = "__all__"