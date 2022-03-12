
def search(users, name):
    for user in users:
        if user['name'] == name:
            return user['age']
    return -1

def main() :
    users = []
    n = int(input("Enter user count: "))
    for i in range(n):
        name = input("Enter the name: ")
        age = input("Enter the age: ")
        print("\n")
        users.append({"name": name,
                       "age": age})
        
    name = input("Enter a name to search: ")
    if(result := search(users, name)) == -1:
        print("user not founc!")
    else :
        print(result)
        
main()
