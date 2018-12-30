from django import forms

Time = [["00:00:00", "00:00:00"],
        ["03:00:00", "03:00:00"],
        ["06:00:00", "06:00:00"],
        ["09:00:00", "09:00:00"],
        ["12:00:00", "12:00:00"],
        ["15:00:00", "15:00:00"],
        ["18:00:00", "18:00:00"],
        ["21:00:00", "21:00:00"],
        ["00:00:00", "00:00:00"],

        ]


class TimeForm(forms.Form):
    from_ = forms.ChoiceField(choices=Time)
    to_ = forms.ChoiceField(choices=Time)

