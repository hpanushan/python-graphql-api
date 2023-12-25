from graphene import Schema, ObjectType, String
import json

"""
{
    name: "Student 1",
    age: 20
}
"""

class Query(ObjectType):
    name = String(value = String(default_value = "Student 0"))
    age = String()
    
    def resolve_name(self, info, value):
        return value
    
    def resolve_age(self, info):
        return "20"


schema = Schema(query=Query)

# specify the query
graphql_query = '''
query myquery {
    student_name: name(value: "Student 10") 
    age
}'''

if __name__ == '__main__':
    result = schema.execute(graphql_query)
    print(json.dumps(result.data, indent=3))
