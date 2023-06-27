#!/usr/bin/env python

# Import the library to do request in HTTP
import requests
# import the library for the HTTP connection requests
import urllib3

# 1.1 Create your user through an HTTP request

# Define subscribe_new_user function to create the new user
def subscribe_new_user(username):
    # Define the user data
    payload = {
        "id": 0,
        "username": username,
        "firstName": "Fabrizia",
        "lastName": "Salvatore",
        "email": "fabriziasalvatore@gmail.com",
        "password": "TareaNNT",
        "phone": "611206900"
    }
    
    # Enable the SSL verification
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    # Make a POST request to create the user. A JSON payload is sent to the /user resource of the API
    create_user_request = requests.post('https://petstore.swagger.io/v2/user', json=payload, verify=False)
    
    # Verify the answer status
    if create_user_request.status_code == 200:
        print("\nUsuario añadido")
    else:
        print("Se produjo un error. El usuario no puede ser añadido")
        
# 1.2 Retrieve the data by calling the corresponding service

    # Make a GET request to retrieve the data of the new user
    retrieve_data_request = requests.get(f'https://petstore.swagger.io/v2/user/{username}', verify=False)
    
    # Verify the answer status, retrieve the data from the JSON answer and print it 
    if retrieve_data_request.status_code == 200:
        user_data = retrieve_data_request.json()       
        print("Datos del usuario:")
        print("ID:", user_data['id'])
        print("Usuario:", user_data['username'])
        print("Nombre:", user_data['firstName'])
        print("Appelido:", user_data['lastName'])
        print("Correo electronico:", user_data['email'])
        print("Móvil:", user_data['phone'])
        print("Contraseña:", user_data['password'])
        print("\n")
    else:
        print("Los datos del usuario no se pueden recuperarprint\n")
        
        
# 2 Retrieve the list of names of the sold pets through an HTTP request

# Define the find_sold_pets function
def find_sold_pets(): 
    # Make a GET request to obtain the list of pets with status sold
    sold_pets_request = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=sold', verify=False)
    
    # Verify the answer status and retrieve the data from the JSON answer
    if sold_pets_request.status_code == 200:
        sold_pets_data = sold_pets_request.json()       
        
        # Create a list of tuples {id, name} for the sold pets checking that the response from the API contains the necessary data
        sold_pets_list = []
        for pet in sold_pets_data:
            pet_id = pet.get('id')
            pet_name = pet.get('name')
            # Check that each pet has id and name keys
            if pet_id and pet_name:
                sold_pets_list.append((pet_id, pet_name))
                
        # Save as tuple the list obtained
        sold_pets_tuple = tuple(sold_pets_list)
        
        # Print the ID and the name for each sold pet
        print("Mascotas vendidas {ID, Name}:")
        
        for pets in sold_pets_tuple:
            print(f"{pets[0]}, {pets[1]}")
        print("\n")            
        return sold_pets_tuple   
    else:
        print("Se produjo un error durante la recuperción de las mascotas vendidas \n")
        return []
        
# 3 Create a class whose constructor requires the mentioned data structure, and implement a method that can iterate through it to identify how many pets have the same name

# Define the class PetCounting taking as input the parameter sold_pets_data
class PetCounting:   
    def __init__(self, sold_pets_data):
        self.sold_pets_data = sold_pets_data   
        
    # Define the method check_pet_name to count the pets with the same name
    def check_pet_name(self):
    
        # Create a dictionary to note all the names and the counts
        name_counter = {}
        
        # Count the number of sold pets with the same name
        for pet in self.sold_pets_data:
            name = pet[1]
            
            # If the name is already as key in the dictionary increment the counter
            if name in name_counter:
                name_counter[name] += 1
            # Else add the name as key to the dictionary and set the counter at 1
            else:
                name_counter[name] = 1
                
        # Print the pets name and the counter
        print("Counting the names of sold pets:")
        for name, count in name_counter.items():
            print(f"{name}: {count}")
        print("\n")


# Use the defined subscribe_new_user function to add the user fsalvatore
subscribe_new_user("fsalvatore")

# Call the find_sold_pets function and assign the returned value to the variable sold_pets
sold_pets =find_sold_pets()

# Create an object PetCounting and pass the list of sold pets as argument
name_pets_counter =PetCounting(sold_pets)

# Call the method check_pet_name to count the number of sold pets with the same name
name_pets_counter.check_pet_name()