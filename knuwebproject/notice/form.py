# class NoticeForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(Notice, self).__init__(*args, **kwargs)
#         self.fields['files '] = forms.FileField(
#             widget=forms.ClearableFileInput(attrs={'multiple': True}),
#         )