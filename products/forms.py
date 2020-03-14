from django  import forms

from .models import Product 

class ProductForm(forms.ModelForm):
	title			=forms.CharField(label='title',widget=forms.TextInput(attrs={"placeholder":"Your Title Here",}))
	description 	=forms.CharField(required=False,widget=forms.Textarea(attrs={
						"class":"new-class-name two",
						"id":"my-text-id-textarea",
						"rows":10,
						'cols':40,
						"placeholder":"Your Description Here"
			}
		)
	)
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price',
			'summary'
		]



class RawProductForm(forms.Form):
	title			=forms.CharField(label='title',widget=forms.TextInput(attrs={"placeholder":"Your Title Here",}))
	description 	=forms.CharField(required=False,widget=forms.Textarea(attrs={
						"class":"new-class-name two",
						"id":"my-text-id-textarea",
						"rows":10,
						'cols':40,
						"placeholder":"Your Description Here"
			}
		)
	)
	price			=forms.DecimalField(initial=00.00)
