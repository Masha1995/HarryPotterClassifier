from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from DatabaseManagerApp.models import Article, NormalizedOrderedWord, NotValuableWord, TextClass
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pickle
import re

print('Text classifier model load... ', end='')
model = pickle.load(open("CheckTextApp/Garry Potter model.dat", 'rb'))
print('ok')

print('Vectorizing context load... ', end='')
not_valuable_words = list(NotValuableWord.objects\
                          .all()\
                          .values_list('word', flat=True))
normalized_ordered_words = list(NormalizedOrderedWord.objects\
                                .all()\
                                .order_by('id')\
                                .values_list('word', flat=True))
print('ok')

def normalize_word(word):
    norm_word = word.lower()
    norm_word = re.sub(r'[.,\/#!\?$%\^&\*;:{}=_`~()]', '', norm_word)
    return norm_word.strip()

def vectorize_text(text):
    text_vector = [0] * len(normalized_ordered_words)
    for text_word in text.split():
        normalized_word = normalize_word(text_word)
        if normalized_word:
            if normalized_word not in not_valuable_words\
               and normalized_word in normalized_ordered_words:
                word_vector_position = normalized_ordered_words.index(normalized_word)
                text_vector[word_vector_position] = text_vector[word_vector_position] + 1
    return np.array([text_vector], int)

def get_possible_class(text):
    result = model.predict(vectorize_text(text))
    return TextClass.objects.get(id = int(result[0]))


def check(request):
    if request.method == "POST":
        user_text = request.POST.get("text")

        result_class = get_possible_class(user_text)
        
        return render(request, "CheckText/checktextresult.html",\
                      context={"result_class": result_class.description})
    else:
        return render(request, "CheckText/checktextform.html")
