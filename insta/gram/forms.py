from.models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user']
        widges = {
        'tags': forms.CheckboxSelectMultiple(),
        }
