from flask import jsonify, request
from flask.views import MethodView

from auth import hash_password, check_auth
from crud import get_user, patch_user, delete_user, create_user, get_ads, create_ads, get_token, patch_ads, delete_ads
from errors import ApiException
from model import Session, User, Token, Ads
from schema import validate, PatchUser, CreateUserSchema, CreateAdsSchema, PatchAds  # , Register


# def register():
#     user_data = validate(Register, request.json)
#     with Session() as session:
#         user_data["password"] = hash_password(user_data["password"])
#         user = create_user(session, User, **user_data)
#         return jsonify({"id": user.id})
#
#
# def login():
#     login_data = validate(Login, request.json)
#     with Session() as session:
#         user = session.query(User).filter(User.email == login_data["email"]).first()
#         if user is None or not check_password(user.password, login_data["password"]):
#             raise ApiError(401, "Invalid user or password")
#
#         token = Token(user=user)
#         session.add(token)
#         session.commit()
#         return jsonify({"token": token.id})
#


class UserView(MethodView):

    def get(self, user_id):
        with Session() as session:
            user = get_user(session, User, user_id)
            return jsonify(
                {"id": user.id, "email": user.email, "registration_time": user.registration_time.isoformat()}
            )

    def post(self):
        user_data = validate(CreateUserSchema, request.json)
        user_data['password'] = hash_password(user_data['password'])
        with Session() as session:
            user = create_user(session, User, **user_data)
            token = Token(user_id=user.id)
            session.add(token)
            session.commit()
            return jsonify({"id": user.id, "token": token.id})


    def patch(self, user_id: int):
        with Session() as session:
            patch_data = validate(PatchUser, request.json)
            if "password" in patch_data:
                patch_data["password"] = hash_password(patch_data["password"])

            token = check_auth(session)
            user = get_user(session, User, user_id)
            if token.user_id != user.id:
                raise ApiException(403, "user has no access")
            user = patch_user(session, user, **patch_data)

            return jsonify(
                {
                    "id": user.id,
                    "email": user.email,
                    "registration_time": user.registration_time.isoformat(),
                }
            )

    def delete(self, user_id: int):
        with Session() as session:
            user = get_user(session, User, user_id)

            token = check_auth(session)
            if token.user_id != user.id:
                raise ApiException(403, "user has no access")

            delete_user(session, user)

            return {"deleted": True}



class AdsView(MethodView):

     def get(self, ads_id: int):
         with Session() as session:
             ads = get_ads(session, Ads, ads_id)
             return jsonify(
                 {"ads_id": ads.id, "title": ads.title,
                  "description": ads.description,
                  "creation_time": ads.creation_time.isoformat(),
                  "user_id": ads.user_id}
             )

     def post(self):
         ads_data = validate(CreateAdsSchema, request.json)
         with Session() as session:
             token = check_auth(session)
             ads_data.update(dict(user_id=token.user_id))
             ads = create_ads(session, Ads, **ads_data)
             session.add(ads)
             session.commit()
             return jsonify(
                 {"ads_id": ads.id, "title": ads.title,
                  "description": ads.description,
                  "creation_time": ads.creation_time.isoformat(),
                  "user_id": ads.user_id}
             )

     def patch(self, ads_id: int):
         ads_data = validate(PatchAds, request.json)
         with Session() as session:
            ads = get_ads(session, Ads, ads_id)
            token_ads = get_token(session, Token, ads.user_id)
            token_in_ads = check_auth(session)
            if token_ads != token_in_ads:
                raise ApiException(403, "user has no access")
            ads = patch_ads(session, ads, **ads_data)

            return jsonify({"ads_id": ads.id, "title": ads.title,
                            "description": ads.description,
                            "creation_time": ads.creation_time.isoformat(),
                            "user_id": ads.user_id}
                            )


     def delete(self, ads_id: int):
        with Session() as session:
            ads = get_ads(session, Ads, ads_id)
            token = check_auth(session)
            if token.user_id != ads.user_id:
                raise ApiException(403, "user has no access")

            delete_ads(session, ads)

            return {"deleted": True}


