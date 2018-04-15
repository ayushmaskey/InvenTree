from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import UniquePart


class EditTrackedPartForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditTrackedPartForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-edit-part-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = UniquePart
        fields = [
            'part',
            'serial',
            'customer',
            'status'
        ]
