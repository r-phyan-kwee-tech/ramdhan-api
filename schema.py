import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import or_, desc, asc

from database import db_session, User as UserModel, Country as CountryModel, State as StateModel, \
    Day as DayModel, gen_offset_from_page, generate_meta


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
        model = StateModel
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

    countries = graphene.Field(lambda: CountryResult, limit=graphene.Int(), page=graphene.Int())
    country = graphene.Field(lambda: Country, country_id=graphene.String(), country_name=graphene.String())

    def resolve_countries(self, args, context, info):
        limit = args.get("limit")
        page = args.get("page")
        all_issue = Country.get_query(context).all()
        result = Country.get_query(context).limit(limit).offset(gen_offset_from_page(page, limit))
        meta_obj = generate_meta(limit, page, all_issue)
        return StateResult(data=result,
                           meta=MetaObject(total_pages=meta_obj["total_page"], current=meta_obj["current"],
                                           prev_page=meta_obj["prev_page"], next_page=meta_obj["next_page"]))

    def resolve_country(self, args, context, info):
        query = Country.get_query(context)
        id = args.get('country_id')
        name = args.get('country_name')
        country = query.filter(or_(CountryModel.object_id == id, (CountryModel.name == name))).first()

        return country

    # issues = SQLAlchemyConnectionField(State)
    states = graphene.Field(lambda: StateResult, limit=graphene.Int(), page=graphene.Int(),
                            country_id=graphene.String())
    state = graphene.Field(lambda: State, state_id=graphene.String()
                           )

    def resolve_states(self, args, context, info):
        limit = args.get("limit")
        page = args.get("page")
        source_id = args.get("country_id")
        all_issue = State.get_query(context).filter(StateModel.country_id == source_id).all()
        result = State.get_query(context).filter(StateModel.country_id == source_id).order_by(
            desc(StateModel.name_mm_uni)).limit(limit).offset(
            gen_offset_from_page(page, limit))
        meta_obj = generate_meta(limit, page, all_issue)
        return StateResult(data=result,
                           meta=MetaObject(total_pages=meta_obj["total_page"], current=meta_obj["current"],
                                           prev_page=meta_obj["prev_page"], next_page=meta_obj["next_page"]))

    def resolve_state(self, args, context, info):
        query = State.get_query(context)
        id = args.get("state_id")
        issue = query.filter(StateModel.object_id == id).first()
        return issue

    day = graphene.Field(lambda: Day, day_id=graphene.String())
    days = graphene.Field(lambda: DayResult, limit=graphene.Int(), page=graphene.Int(),
                          state_id=graphene.String())

    def resolve_days(self, args, context, info):
        limit = args.get("limit")
        page = args.get("page")
        issue_id = args.get("state_id")
        all_issue = Day.get_query(context).filter(DayModel.state_id == issue_id).all()
        result = Day.get_query(context).filter(DayModel.state_id == issue_id).order_by(asc(DayModel.day)).limit(
            limit).offset(
            gen_offset_from_page(page, limit))
        meta_obj = generate_meta(limit, page, all_issue)
        return DayResult(data=result,
                         meta=MetaObject(total_pages=meta_obj["total_page"], current=meta_obj["current"],
                                         prev_page=meta_obj["prev_page"], next_page=meta_obj["next_page"]))

    def resolve_day(self, args, context, info):
        query = Day.get_query(context)
        id = args.get("day_id")
        day = query.filter(DayModel.object_id == id).first()
        return day

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
