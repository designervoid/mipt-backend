from django.shortcuts import render
from .models import Claim
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer , TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import pickle


# Create your views here.
def old(request):
    context = {}
    return render(request, 'old.html', context)


class ML_AGH():
    def __init__(self, message):
        self.text_clf = Pipeline([
                             ('tfidf', TfidfVectorizer()),
                             ('clf', RandomForestClassifier(n_estimators=250))
                             ])
        self.switcher = {
            0: "сантехник",
            1: "уборщица",
            2: "электрик",
            3: "дезинсектор",
            4: "охранник",
            5: "медсестра",
            6: "плотник"
        }
        self.message = message
        self.texts = [['cантехник','раковина','ремонт сантехнического оборудования','cломалась машинка', 'починить машинку', 'стиральная машинка',
          'промывка системы отопления перед началом отопительного сезона','своевременная замена изношенных узлов, частей и деталей','устранение засоров в трубах водоснабжения и канализации',
          'монтаж, установка, настройка сантехники,','потек кран', 'засорился унитаз' ,'надо срочно вызывать сантехника','перекрыть воду','не смывается туалет', 'засорение раковины', 'вода туалет ванна', 'начал подтекать кран ','течет унитаз', 'протечка стояков' ],
         ['электрик','перегорели провода','розетки', 'проводка и нагрузка на сеть', 'выключили свет', 'перепабды напряжения', 'работа с электроприборами', 'короткое замыкание'],
         ['санитарная обработка', 'санитар','муравьи', 'тараканы', 'насекомые', 'мухи', 'животные', 'дезинфекционная', 'уничтожение паразитов', 'жуки', 'убить насекомых', 'завелись грызуны и мыши'],
         ['плотник', 'ножка стула', 'ручка', 'дверь', 'починить стул', 'кровать', 'сломался стул'],
         ['заказать мебель', 'тумбочка', 'заказать стул', 'заказать стол', 'заказать шкаф'],
         ['крупногабаритные вещи', 'ввоз', 'вывоз', 'внести', 'вынести', 'заезд', 'выезд', 'холодильник']]

    def proc_data(self):
        text=[]
        texts_labels=[]
        for i in range(len(self.texts)):
            texts_labels += [i]*len(self.texts[i])
            text+=self.texts[i]
        return text, texts_labels

    def TfidVector_RandomForestCl(self):
        text, texts_labels = self.proc_data()
        self.text_clf.fit(text, texts_labels)


    def save_state_ML(self):
        message='сломался стул '
        with open('save_ml/text_clf', 'wb') as picklefile:
            pickle.dump(self.text_clf, picklefile)
        with open('save_ml/text_clf', 'rb') as training_model:
            model = pickle.load(training_model)
        res = self.text_clf.predict([message])
        self.switcher.get(res[0])



def new(request):
    message = [ q.executor for q in Claim.objects.all() ]
    ml = ML_AGH(message)
    ml.proc_data()
    ml.TfidVector_RandomForestCl()
    ml.save_state_ML()
    return render(request, 'new.html', context={})

def feedback(request):
    return render(request, 'feedback.html', context={})