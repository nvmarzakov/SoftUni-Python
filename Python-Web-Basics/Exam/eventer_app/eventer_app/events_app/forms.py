from django import forms

from .models import EventModel


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = '__all__'
        labels = {
            'event_name': 'Name',
            'category': 'Category',
            'description': 'Description',
            'date': 'Date',
            'event_image': 'Event Image',
        }


class EventCreateForm(EventBaseForm):
    pass


class EventEditForm(EventBaseForm):
    pass


class EventDeleteForm(EventBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
