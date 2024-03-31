#!/usr/bin/python3
'''Something useful'''
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, database),
            pool_pre_ping=True,
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Something more useful'''
        if cls is None:
            obj = self.__session.query(State).all()
            obj.extend(self.__session.query(User).all())
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(Review).all())
            obj.extend(self.__session.query(Amenity).all())
        else:
            if isinstance(cls, str):
                cls = eval(str)
            obj = self.__session.query(cls)
        return {"{}.{}"
                .format(i.__class__.__name__, i.id): i for i in obj}

    def new(self, obj):
        '''Something more useful'''
        self.__session.add(obj)

    def save(self):
        '''Something more useful'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Something more useful'''
        if obj is not None:
            self.__session.delete()

    def reload(self):
        '''Something more useful'''
        Base.metadata.create_all(self.__engine)
        current_session = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(current_session)
        self.__session = Session()

    def close(self):
        '''Something more useful'''
        self.__session.close()
