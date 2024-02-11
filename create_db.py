import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import create_tables, User, Word, CommonWord
import configparser



def create_db(engine):

    common_words = (
        ('Dog', 'Собака'),
        ('Cat', 'Кошка'),
        ('Car', 'Машина'),
        ('Table', 'Стол'),
        ('White', 'Белый'),
        ('Red', 'Красный'),
        ('Blue', 'Синий'),
        ('He', 'Он'),
        ('She', 'Она'),
        ('They', 'Они')
    )

    create_tables(engine)

    session = (sessionmaker(bind=engine))()

    for row in common_words:
        session.add(CommonWord(word=row[0], translate=row[1]))
    session.commit()
    session.close()
    
config = configparser.ConfigParser()
config.read('settings.ini')

engine = sq.create_engine(config['posgres']['DSN'])

create_db(engine)