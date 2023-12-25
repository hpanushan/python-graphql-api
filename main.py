from graphene import Schema, ObjectType, String, Int, Field

class CustomerType(ObjectType):
    id = Int()
    name = String()
    age = Int()

class Query(ObjectType):
    user = Field(CustomerType, id=Int(default_value = 1))

    # dummy data store
    users = [
        {"id": 1, "name": "Alan", "age": 20},
        {"id": 2, "name": "Bob", "age": 30},
        {"id": 3, "name": "Cathy", "age": 40},
    ]
    def resolve_user(self, info, id):
        matched_users = [user for user in Query.users if user["id"] == id]
        return matched_users[0] 

schema = Schema(query=Query)

graphql_query = '''
query myquery {
    user(id: 2) {
        id
        name
        age
    }
}
'''

if __name__ == '__main__':
    result = schema.execute(graphql_query)
    print(result)
