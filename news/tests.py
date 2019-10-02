from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.lavender = Editor(first_name = 'Lavender',last_name ='Chemutai',email='lavenderchems@gmail.com')
        

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.lavender,Editor))

    #testing save method
    def test_save_method(self):
        self.lavender.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
    
    #testing delete method
   # def test_delete_method(self):
        #self.lavender.delete_editor()
        #editors = Editor.objects.all()
        #self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):
    def setUp(self):
        #creating a new editor and saving it
        self.lavender = Editor(first_name = 'Lavender',last_name = 'Chemutai',email = 'lavenderchems@gmail.com' )
        self.lavender.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()
        #creating a new article and saving it
        self.new_article = Article(title = 'Test Article',post = 'This is a random test Post',editor = self.lavender)

        self.new_article.save()
        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)
    
    def test_get_news_by_date( self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)