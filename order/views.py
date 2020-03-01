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
        print('\n\n\n\n\n\n\n\n\n\n\n\nn\n\n\ninit')
        self.message = message
        self.texts = [['cантехник','ремонт сантехнического оборудования','cломалась машинка', 'починить машинку', 'стиральная машинка',
                  'промывка системы отопления перед началом отопительного сезона','своевременная замена изношенных узлов, частей и деталей','устранение засоров в трубах водоснабжения и канализации',
                  'монтаж, установка, настройка сантехники,','потек кран', 'засорился унитаз' ,'надо срочно вызывать сантехника','перекрыть воду','не смывается туалет', 'засорение раковины', 'вода туалет ванна', 'начал подтекать кран ','течет унитаз', 'протечка стояков' ],
                 ['уборщица','удаление пыли и грязи','полы','почистить','помыть окна', 'мытье посуды','нужно помыть посуду', 'грязно мусор пыль нужно убрать ', 'чистка пылесосом ковров и мебели', 'удаление масляных пятен','жир, нагар на кухне'],
                 ['электрик','перегорели провода','розетки', 'проводка и нагрузка на сеть', 'выключили свет', 'перепабды напряжения', 'работа с электроприборами', 'короткое замыкание'],
                 ['дезинсектор','муравьи', 'тараканы', 'насекомые', 'мухи', 'животные', 'дезинфекционная', 'уничтожение паразитов', 'жуки', 'убить насекомых', 'завелись грызуны и мыши'],
                 ['охранник','разбойник', 'вор', 'драка', 'громкая музыка',  'крики', 'разбили стекло', 'мешают', 'происшествие', 'опасность', 'правоохранительные органы'],
                 ['врач','медсестра','кровь','плохо чувствую', 'температура', 'болит голова', 'кашель', 'насморк', 'нога', 'сломал ножку'],
                 ['плотник', 'ножка стула', 'ручка', 'стол', 'cтул', 'дверь', 'починить', 'кровать', 'сломался стул']]

    def proc_data(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\nn\n\n\nprocdata')
        text=[]
        texts_labels=[]
        for i in range(len(self.texts)):
            texts_labels += [i]*len(self.texts[i])
            text+=self.texts[i]
        return text, texts_labels

    def TfidVector_RandomForestCl(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\nn\n\n\nTfid')
        text, texts_labels = self.proc_data()
        self.text_clf.fit(text, texts_labels)


    def save_state_ML(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\nn\n\n\nsave_state')
        message='сломался стул '
        with open('text_clf', 'wb') as picklefile:
            pickle.dump(self.text_clf, picklefile)
        with open('text_clf', 'rb') as training_model:
            model = pickle.load(training_model)
        res = self.text_clf.predict([message])
        print(self.switcher.get(res[0]))



def new(request):
    message = [ q.executor for q in Claim.objects.all() ]
    ml = ML_AGH(message)
    ml.proc_data()
    ml.TfidVector_RandomForestCl()
    ml.save_state_ML()
    return render(request, 'new.html', context={})

def feedback(request):
    return render(request, 'feedback.html', context={})