import uuid
from Database import Database
class history(object):

    def __init__(self,email,description,host,keywords,title,url,timestamp,count=1,_id=None):
        self.email = email
        self.description = description
        self.host = host
        self.keywords = keywords
        self.title = title
        self.url = url
        self.timestamp = timestamp
        self.count = count
        self._id = uuid.uuid4().hex if id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='history',data=self.json())

    def json(self):
        return {
            'email':self.email,
            'description':self.description,
            'host': self.host,
            'keywords': self.keywords,
            'title': self.title,
            'url': self.url,
            'timestamp': self.timestamp,
            'count': self.count,
            '_id':self._id
        }

    @classmethod
    def getRecordByTitle(cls,title):
        recordHistory =  Database.find_one(collection='history',query={'title':title})
        return cls(**recordHistory)
