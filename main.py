import Pet

def main():

    print_header()
    print('hey')
    print_footer(2)
    
    pet_list = []
    
    
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
            view_all()
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
            print(f'{pet_list}')
            
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass


def view_all(pet_list):
    print_header()
    
    print_footer()
    

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