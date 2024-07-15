import Pet

def main():

    pet_list = []
    
    while True:
        
        print("""What would you like to do?
            1) View all pets
            2) Add more pets
            3) Update an existing pet.
            4) Remove an existing pet
            5) Search pets by name
            6) Search pets by age
            7) Exit program
            """)
        
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:        
                view_all(pet_list)
            case 2:
                
                added_counter = 0
                
                while True:
                    
                    pet_string = input('add pet (name, age): ')
                    
                    if pet_string == 'done':
                        break
                    
                    pet_info = parse_pet(pet_string)
                    pet_list.append(Pet.Pet(pet_info[0],pet_info[1]))
                    
                    added_counter += 1
                
                print(f'{added_counter} pets added')             
                
            case 3:
                
                view_all(pet_list)
                
                pet_id = int(input('Enter the pet ID you want to update: '))
                pet_string = input('update pet (name, age): ')
                
                pet_info = parse_pet(pet_string)
                
                old_name = pet_list[pet_id].name
                old_age = pet_list[pet_id].age
                
                pet_list[pet_id].set_name(pet_info[0])
                pet_list[pet_id].set_age(pet_info[1])
                
                print(f'{old_name} {old_age} changed to {pet_info[0]} {pet_info[1]}\n' )
                
            case 4:
                
                view_all(pet_list)
                
                pet_id = int(input('Enter the pet ID you want to delete: '))
                
                old_name = pet_list[pet_id].name
                old_age = pet_list[pet_id].age
                
                pet_list.pop(pet_id)
                
                print(f'{old_name} {old_age} removed')
                
            case 5:
                
                found_list = []
                name = input('Enter name to search: ').lower()
                
                for pet in pet_list:
                    
                    if pet.name.lower() == name:
                        found_list.append(pet)
                
                if len(found_list) > 0:
                    view_all(found_list)
                else:
                    print(f'No pets named {name}.')
                    
                    
            case 6:
                
                found_list = []
                age = int(input('Enter age to search: '))
                
                for pet in pet_list:
                    
                    if int(pet.age) == age:
                        found_list.append(pet)
                
                if len(found_list) > 0:
                    view_all(found_list)
                else:
                    print(f'No pets aged {age}.')            
            
            case 7:
                quit()
                


def view_all(pet_list):
    
    print_header()
    
    for pet in pet_list:
        print(f"| {pet.id:<3}| {pet.name:<10}| {pet.age:<4}|")

    print_footer(len(pet_list))
    

def parse_pet(pet_string):
    return pet_string.strip().split()

def print_footer(count):
    print(f"+{'-'*22}+")
    print(f"{count} rows in set.")

def print_header():
    
    print(f"+{'-'*22}+")
    print(f"| ID | Name      | AGE |")
    print(f"+{'-'*22}+")

    

main()