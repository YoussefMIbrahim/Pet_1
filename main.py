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
    
    case = int(input("Enter your choice: "))
    
    def switch_case(case):
        if case == 1:
            pass
        if case == 2:
            
            added_counter = 0
            
            while True:
                
                pet_string = input('add pet (name, age): ')
                
                if pet_string == 'done':
                    break
                
                pet_info = parse_pet(pet_string)
                print(pet_info)
                
                added_counter += 1
            
            print(f'{added_counter} pets added')
                
                
        if case == 3:
            pass
        if case == 4:
            pass
        if case == 5:
            pass
        if case == 6:
            pass
        if case == 7:
            pass


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