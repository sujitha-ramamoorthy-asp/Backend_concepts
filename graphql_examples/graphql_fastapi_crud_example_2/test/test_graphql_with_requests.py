import requests

url = "http://127.0.0.1:8000/graphql"

query = """
mutation {
  login(
    username: "admin",
    password: "admin123"
  ) {
    accessToken
    tokenType
  }
}
"""

response = requests.post(
    url,
    json={"query": query}
)

print(response.json())

token = response.json()["data"]["login"]["accessToken"]

print(token)

query = """
query{
    me{
        id
        username
        role
    }
}
"""

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.post(
    url,
    json={"query": query},
    headers=headers
)

print(response.json())

query = """
mutation{

    createEmployee(

        name:"John"

        salary:65000

    ){

        id

        name

        salary

    }

}
"""

headers = {

    "Authorization": f"Bearer {token}"

}

response = requests.post(

    url,

    json={"query": query},

    headers=headers

)

print(response.json())

# using variables
#Instead of embedding values directly in the GraphQL query, use variables.
query = """
mutation CreateEmployee(
    $name:String!,
    $salary:Int!
){

    createEmployee(

        name:$name

        salary:$salary

    ){

        id

        name

    }

}
"""

variables = {

    "name":"David",

    "salary":90000

}

response = requests.post(

    url,

    json={

        "query":query,

        "variables":variables

    },

    headers=headers

)

print(response.json())