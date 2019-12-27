from django.shortcuts import render
from DatabaseManagerApp.models import NormalizedOrderedWord, NotValuableWord, TextClass
import numpy as np
import pickle
import re

# загрузка обученной модели классификатора
print('Text classifier model load... ', end='')
model = pickle.load(open("CheckTextApp/Garry Potter model.dat", 'rb'))
print('ok')

# загрузка словарей
print('Vectorizing context load... ', end='')
# загрузка слов на фильтрацию, чтобы их отбросить
not_valuable_words = list(NotValuableWord.objects\
                          .all()\
                          .values_list('word', flat=True))
# загрузка списка слов из заранее сформированной "сумки слов"
normalized_ordered_words = list(NormalizedOrderedWord.objects\
                                .all()\
                                .order_by('id')\
                                .values_list('word', flat=True))
print('ok')

def normalize_word(word):
    norm_word = word.lower()
    norm_word = re.sub(r'[.,\/#!\?$%\^&\*;:{}=_`~()\'"\-\[\]«»<>]', '', norm_word)
    norm_word = norm_word.strip()
    if re.match(r'^[а-яА-Я]+$', norm_word):
        return norm_word
    else:
        return ''

def vectorize_text(text):
    text_vector = [0] * len(normalized_ordered_words)
    for text_word in text.split():
        normalized_word = normalize_word(text_word)
        if normalized_word:
            if normalized_word not in not_valuable_words and normalized_word in normalized_ordered_words:
                word_vector_position = normalized_ordered_words.index(normalized_word)
                text_vector[word_vector_position] = text_vector[word_vector_position] + 1
    return np.array([text_vector], int)

def get_possible_class(text):
    result = model.predict(vectorize_text(text))
    return TextClass.objects.get(id = int(result[0]))


def valide_text(text):
    for text_word in text.split():
        normalized_word = normalize_word(text_word)
        if normalized_word:
            return True
    return False


def check(request):
    if request.method == "POST":
        user_text = request.POST.get("text")
        if valide_text(user_text):
            result_class = get_possible_class(user_text)

            return render(request, "CheckText/checktextresult.html", \
                          context={"result_class": result_class.description})
        else:
            return render(request, "CheckText/checktexterror.html")
    else:
        return render(request, "CheckText/checktextform.html")
