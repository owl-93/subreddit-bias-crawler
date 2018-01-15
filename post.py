class Post:
    title = None
    date = None
    score = None
    user = None
    domain = None

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def setUser(self, user):
        self.user = user

    def getUser(self):
        return self.user

    def setDomain(self, domain):
        self.domain = domain

    def getDomain(self):
        return self.domain