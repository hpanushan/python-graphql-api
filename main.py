from graphene import Schema, ObjectType, String, Int, Field, List, Mutation

class CustomerType(ObjectType):
    id = Int()
    name = String()
    age = Int()

class CreateCustomer(Mutation):
    class Arguments:
        name = String()
        age = Int()

    customer = Field(CustomerType)
    @staticmethod
    def mutate(root, info, name, age):
        customer = {
            "id": len(Query.customers) + 1,
            "name": name,
            "age": age,
        }
        Query.customers.append(customer)
        return CreateCustomer(customer=customer)

class UpdateCustomer(Mutation):
    class Arguments:
        id = Int(required=True)
        name = String()
        age = Int()
    
    customer = Field(CustomerType)

    @staticmethod
    def mutate(root, info, id, name=None, age=None):

        for customer in Query.customers:
            if customer["id"] == id:
                if name:
                    customer["name"] = name
                if age:
                    customer["age"] = age
                return UpdateCustomer(customer=customer)

class DeleteCustomer(Mutation):
    class Arguments:
        id = Int(required=True)
    
    customer = Field(CustomerType)

    @staticmethod
    def mutate(root, info, id):
        for customer in Query.customers:
            if customer["id"] == id:
                Query.customers.remove(customer)
                return DeleteCustomer(customer=customer)

class Query(ObjectType):
    customer = Field(CustomerType, id=Int(default_value = 1))
    customer_all = List(CustomerType)
    customer_by_min_age = List(CustomerType, min_age=Int(default_value = 20))

    # dummy data store
    customers = [
        {"id": 1, "name": "Alan", "age": 20},
        {"id": 2, "name": "Bob", "age": 30},
        {"id": 3, "name": "Cathy", "age": 40},
    ]
    @staticmethod
    def resolve_customer(root, info, id):
        matched_customers = [customer for customer in Query.customers if customer["id"] == id]
        return matched_customers[0] 
    
    @staticmethod
    def resolve_customer_all(root, info):
        return Query.customers
    
    @staticmethod
    def resolve_customer_by_min_age(root, info, min_age):
        matched_customers = [customer for customer in Query.customers if customer["age"] >= min_age]
        return matched_customers

class Mutation(ObjectType):
    create_customer = CreateCustomer.Field()
    update_customer = UpdateCustomer.Field()
    delete_customer = DeleteCustomer.Field()

schema = Schema(query=Query, mutation=Mutation, auto_camelcase=True)

read_all_customers_graphql_query = '''
query myquery {
    customerAll{
        id
        name
        age
    }
}
'''

read_customer_by_id_graphql_query = '''
query myquery {
    customer (id: 1) {
        id
        name
        age
    }
}
'''

create_customer_graphql_query = '''
mutation mymutation {
    createCustomer(name: "Kate", age: 15) {
        customer {
            id
            name
            age
        }
    }
}
'''

update_customer_graphql_query = '''
mutation mymutation {
    updateCustomer(id: 1, name: "Kate", age: 15) {
        customer {
            id
            name
            age
        }
    }
}
'''

delete_customer_graphql_query = '''
mutation mymutation {
    deleteCustomer(id: 1) {
        customer {
            id
            name
            age
        }
    }
}
'''



if __name__ == '__main__':
    result = schema.execute(delete_customer_graphql_query)
    print(result)

    result = schema.execute(read_all_customers_graphql_query)
    print(result)
