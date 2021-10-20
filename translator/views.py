from django.shortcuts import render

# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_text']
        output = original_text.upper()
        return render(request, 'translator.html', {'input_text': original_text, 'output_text': output})
    else:
        return render(request, 'translator.html')