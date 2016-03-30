from django import forms

class ContactForm(forms.Form):
    OPTIONS = (
                ("M", "Male"),
                ("F", "Female"),
                )
    gender = forms.ChoiceField(choices=OPTIONS)
    OPTIONS_DIST = (
                ("0", "100 metres"),
                ("1", "200 metres"),
                ("2", "400 metres"),
                ("3", "800 metres"),
                ("4", "1500 metres"),
                ("5", "Mile"),
                ("6", "5 km"),
                ("7", "10 km"),
                ("8", "Half-Marathon"),
                ("9", "Marathon"),
                )
    distance1 = forms.ChoiceField(choices=OPTIONS_DIST)
    time1 = forms.FloatField()
    distance2 = forms.ChoiceField(choices=OPTIONS_DIST)
    time2 = forms.FloatField()
    distance3 = forms.ChoiceField(choices=OPTIONS_DIST)
    time3 = forms.FloatField()
    distanceToPredict = forms.ChoiceField(choices=OPTIONS_DIST)
