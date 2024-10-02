import re

from django.shortcuts import render
from django.http import HttpResponse
from .models import WordCount


# Create your views here.


def index(request):
    return render(request, 'word_counter/index.html')


def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        text = file.read().decode('utf-8')
        words = re.findall(r'\b[a-zA-Zа-яА-Я]+\b', text)
        for word in words:
            word_lower = word.lower()
            word_count, created = WordCount.objects.get_or_create(word=word_lower)
            word_count.count += 1
            word_count.save()
        return HttpResponse('File uploaded successfully!')
    return HttpResponse('Invalid request')


def word_count(request):
    if request.method == 'POST':
        word = request.POST['word']
        word_lower = word.lower()
        try:
            word_count = WordCount.objects.get(word=word_lower)
            return HttpResponse(f'The word "{word}" was found {word_count.count} times.')
        except WordCount.DoesNotExist:
            return HttpResponse(f'The word "{word}" was not found.')
    return HttpResponse('Invalid request')


def clear_data(request):
    WordCount.objects.all().delete()
    return HttpResponse('Data cleared successfully!')
