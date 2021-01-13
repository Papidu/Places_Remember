from .models import RememberCards
# from django.forms import TextInput, Textarea, FileInput
from django.contrib.gis.forms import TextInput, Textarea, FileInput, ModelForm,OSMWidget,PointField


class RememberForm(ModelForm):
    location = PointField(widget=OSMWidget(attrs={'map_width': 800, 'map_height': 500}))

    class Meta:
        model = RememberCards

        fields = ['location_name',  'image', 'notes']

        widgets = {
            "location_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Воспоминание о "
            }),
            "image": FileInput,
            "notes": Textarea(attrs={
                "class": "Вставте фотографию",
                "placeholder": "Заметки"
            })
        }
