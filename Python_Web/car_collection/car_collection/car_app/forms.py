from django import forms

from car_collection.car_app.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        # for fields take all fields from model
        fields = '__all__'
        labels = {
            'image_url': 'Image URL:'
        }
