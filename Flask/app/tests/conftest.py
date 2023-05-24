import time

from pytest import fixture

from model import Base, engine, Session, User, Token


@fixture(scope='session', autouse=True)
def prepare_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


@fixture()
def create_user():
    with Session() as session:
        new_user = User(email=f'User_1@test.ru', password='Toefa34532!ddDd23')
        new_token = Token(user_id=1)
        session.add(new_user)
        session.add(new_token)
        session.commit()
        return {'email': new_user.email,
                'id': new_user.id,
                "registration_time": new_user.registration_time
                # 'token': Token(user_id=new_user.id)
                }