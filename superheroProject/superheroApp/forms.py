from django import forms
from .models import superheroApplication

areyourichordoyouhavesuperpowers=(
    (0,'Neither'),
    (1,'No I am not rich,but I have superpowers'),
    (2,'Yes I am rich,and i do not have superpowers'),

)
whichonebestfitsyou=(
    (0,'Good'),
    (1,'KindaGood'),
    (2,'neutral'),
    (3,'little evil'),
    (4,'all the way evil'),
)
Super_Powers=(
    (0,'None'),
    (1, 'Super Speed'),
    (2, "You can Fly"),
    (3,"Healing Abilities"),
    (4,"Look into the future"),
)


class superheroApplicationForm(forms.ModelForm):
    class Meta:
        model=superheroApplication
        fields= "__all__"
        widgets={
            # "dropbox":forms.Select(choices=areyourichordoyouhavesuperpowers),
            "whichofthefollowingareyou":forms.Select(choices=whichonebestfitsyou),
            "areyourichordoyouhavesuperpowers": forms.Select(choices=areyourichordoyouhavesuperpowers),
            "ifyouhavesuperpowerwhichones":forms.SelectMultiple(choices=Super_Powers),
            "give_us_3_examples_when_you_used_your_super_ablities":forms.Textarea(attrs=[])

        }
        labels={
            'areyourichordoyouhavesuperpowers':"Are you rich or do you have super powers.",
            'whichofthefollowingareyou':"Which of the following best fits you?",
            "ifyouhavesuperpowerwhichones":"If you have Super Powers which ones?"


        }