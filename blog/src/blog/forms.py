from django import forms
from .models import Post


class SimplePostForm(forms.Form):
    title = forms.CharField()
    slug = forms.CharField()
    content = forms.TextInput()
    hero_image = forms.ImageField()
    ...

    class Meta:
        fields = ("title", "slug", "content", "hero_image")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "slug", "content", "hero_image", "status", "owner")
        # exclude = (
        #     "created_at",
        #     "updated_at"
        # )
