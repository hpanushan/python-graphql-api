from graphene import Schema, ObjectType, String, Int

def main():

    class Query(ObjectType):
        name = String(value=String(default_value = "Student 0"))
        age = Int(value=Int(default_value = 20))
        message = String(value=String(default_value ="world"))

        def resolve_name(self, info, value):
            return value
        
        def resolve_age(self, info, value):
            return value
        
        def resolve_message(self, info, value):
            return "Hello " + value

    schema = Schema(Query)

    graphql_schema = '''
    query myquery {
        studnt_name: name(value:"Student 10") 
        message(value:"Anushan")
    }
    '''

    print(schema.execute(graphql_schema))

if __name__ == '__main__':
    main()
