import calendar
import datetime

import graphene
from flask import render_template
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from pip._vendor import requests
from pyquery import PyQuery as pq
from readability import Document
from sqlalchemy import or_, desc

from database import db_session, User as UserModel, Country as CountryModel, State as StateModel, \
    Day as DayModel, gen_offset_from_page, generate_meta
from readingtime import ReadingTime


class Users(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)


class Country(SQLAlchemyObjectType):
    class Meta:
        model = CountryModel 
        interfaces = (relay.Node,)


class State(SQLAlchemyObjectType):
    class Meta:
        model =StateModel 
        interfaces = (relay.Node,)


class Day(SQLAlchemyObjectType):
    class Meta:
        model = DayModel
        interfaces = (relay.Node,)


class MetaObject(graphene.ObjectType):
    total_pages = graphene.Int()
    current = graphene.Int()
    prev_page = graphene.Int()
    next_page = graphene.Int()


class CountryResult(graphene.ObjectType):
    meta = graphene.Field(MetaObject)
    data = graphene.List(of_type=Country)


class StateResult(graphene.ObjectType):
    meta = graphene.Field(MetaObject)
    data = graphene.List(of_type=State)


class DayResult(graphene.ObjectType):
    meta = graphene.Field(MetaObject)
    data = graphene.List(of_type=Day)


# Used to Create New User
class createUser(graphene.Mutation):
    class Input:
        name = graphene.String()
        email = graphene.String()
        username = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(Users)

    @classmethod
    def mutate(cls, _, args, context, info):
        user = UserModel(name=args.get('name'), email=args.get('email'), username=args.get('username'))
        db_session.add(user)
        db_session.commit()
        ok = True
        return createUser(user=user, ok=ok)


# Used to Change Username with Email
class changeUsername(graphene.Mutation):
    class Input:
        username = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(Users)

    @classmethod
    def mutate(cls, _, args, context, info):
        query = Users.get_query(context)
        email = args.get('email')
        username = args.get('username')
        user = query.filter(UserModel.email == email).first()
        user.username = username
        db_session.commit()
        ok = True

        return changeUsername(user=user, ok=ok)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # user = SQLAlchemyConnectionField(Users)

    sources = graphene.Field(lambda: CountryResult, limit=graphene.Int(), page=graphene.Int())
    source = graphene.Field(lambda: Country, source_id=graphene.String(), source_name=graphene.String())

    def resolve_sources(self, args, context, info):
        limit = args.get("limit")
        page = args.get("page")
        all_issue = Country.get_query(context).all()
        result = Country.get_query(context).limit(limit).offset(gen_offset_from_page(page, limit))
        meta_obj = generate_meta(limit, page, all_issue)
        return StateResult(data=result,
                           meta=MetaObject(total_pages=meta_obj["total_page"], current=meta_obj["current"],
                                           prev_page=meta_obj["prev_page"], next_page=meta_obj["next_page"]))

    def resolve_source(self, args, context, info):
        query = Country.get_query(context)
        id = args.get('source_id')
        name = args.get('source_name')
        source = query.filter(or_(CountryModel.object_id == id, (CountryModel.name == name))).first()

        return source

    # issues = SQLAlchemyConnectionField(State)
    issues = graphene.Field(lambda: StateResult, limit=graphene.Int(), page=graphene.Int(), source_id=graphene.String())
    issue = graphene.Field(lambda: State, issue_id=graphene.String(), url=graphene.String(),
                           issue_number=graphene.String())

    def resolve_issues(self, args, context, info):
        limit = args.get("limit")
        page = args.get("page")
        source_id = args.get("source_id")
        all_issue = State.get_query(context).filter(StateModel.source_id == source_id).all()
        result = State.get_query(context).filter(StateModel.source_id == source_id).order_by(
            desc(StateModel.issue_number)).limit(limit).offset(
            gen_offset_from_page(page, limit))
        meta_obj = generate_meta(limit, page, all_issue)
        return StateResult(data=result,
                           meta=MetaObject(total_pages=meta_obj["total_page"], current=meta_obj["current"],
                                           prev_page=meta_obj["prev_page"], next_page=meta_obj["next_page"]))

    def resolve_issue(self, args, context, info):
        query = State.get_query(context)
        id = args.get("issue_id")
        url = args.get("issue_url")
        issue_number = args.get("issue_number")
        issue = query.filter(
            or_(StateModel.object_id == id, (StateModel.url == url),
                (StateModel.issue_number == issue_number))).first()
        return issue

    article = graphene.Field(lambda: Day, article_id=graphene.String(), article_content=graphene.String())
    articles = graphene.Field(lambda: DayResult, limit=graphene.Int(), page=graphene.Int(),
                              issue_id=graphene.String())

    def resolve_articles(self, args, context, info):
        limit = args.get("limit")
        page = args.get("page")
        issue_id = args.get("issue_id")
        all_issue = Day.get_query(context).filter(DayModel.issue_id == issue_id).all()
        result = Day.get_query(context).filter(DayModel.issue_id == issue_id).limit(limit).offset(
            gen_offset_from_page(page, limit))
        meta_obj = generate_meta(limit, page, all_issue)
        return DayResult(data=result,
                         meta=MetaObject(total_pages=meta_obj["total_page"], current=meta_obj["current"],
                                             prev_page=meta_obj["prev_page"], next_page=meta_obj["next_page"]))

    def resolve_article(self, args, context, info):
        query = Day.get_query(context)
        id = args.get("article_id")
        title = args.get("article_content")
        article = query.filter(
            or_(DayModel.object_id == id, (DayModel.title.like("%title%")))).first()
        return article

    # find_user = graphene.Field(lambda: Users, username=graphene.String())
    # all_users = SQLAlchemyConnectionField(Users)

    def resolve_find_user(self, args, context, info):
        query = Users.get_query(context)
        username = args.get('username')
        return query.filter(UserModel.username == username).first()


class MyMutations(graphene.ObjectType):
    create_user = createUser.Field()
    change_username = changeUsername.Field()


schema = graphene.Schema(query=Query, types=[Country, State, Day])
