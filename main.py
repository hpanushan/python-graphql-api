from graphene import Schema, ObjectType, String, Int, Field, List

class CustomerType(ObjectType):
    id = Int()
    name = String()
    age = Int()

class Query(ObjectType):
    user = Field(CustomerType, id=Int(default_value = 1))
    users_by_min_age = List(CustomerType, min_age=Int(default_value = 20))

    # dummy data store
    users = [
        {"id": 1, "name": "Alan", "age": 20},
        {"id": 2, "name": "Bob", "age": 30},
        {"id": 3, "name": "Cathy", "age": 40},
    ]
    @staticmethod
    def resolve_user(root, info, id):
        matched_users = [user for user in Query.users if user["id"] == id]
        return matched_users[0] 
    
    @staticmethod
    def resolve_users_by_min_age(root, info, min_age):
        matched_users = [user for user in Query.users if user["age"] >= min_age]
        return matched_users

schema = Schema(query=Query, auto_camelcase=True)

graphql_query = '''
query myquery {
    usersByMinAge(minAge: 34) {
        id
        name
        age
    }
}
'''

if __name__ == '__main__':
    result = schema.execute(graphql_query)
    print(result)
