class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, '_title') and len(title) >= 4 and len(title) <= 50:
            self._title = title
        else:
            return None
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            return None
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            return None
        
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, '_name') and name and isinstance(name, str):
            self._name = name
        else:
            return None

    # def articles(self):
    #     written_articles = []
    #     if isinstance(self, Article):
    #         for article in self._articles:


    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if len(str(name)) >= 2 and len(str(name)) <= 16 and isinstance(name, str):
            self._name = name
        else:
            return None
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if len(category) > 0 and isinstance(category, str):
            self._category = category
        else:
            return None

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass