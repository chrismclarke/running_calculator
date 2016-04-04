from django import forms

class ContactForm(forms.Form):
    OPTIONS = (
                ("M", "Male"),
                ("F", "Female"),
                )
    gender = forms.ChoiceField(choices=OPTIONS)
    OPTIONS_DIST = (
                ("None","NONE"),
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
    distance1 = forms.ChoiceField(choices=OPTIONS_DIST,label='Distance A')
    time1 = forms.FloatField(initial=0,label='Time A')
    distance2 = forms.ChoiceField(choices=OPTIONS_DIST,label='Distance B')
    time2 = forms.FloatField(initial=0, label='Time B')
    distance3 = forms.ChoiceField(choices=OPTIONS_DIST,label='Distance C')
    time3 = forms.FloatField(initial=0, label='Time C')
    distanceToPredict = forms.ChoiceField(choices=OPTIONS_DIST,label='Distance to predict')
