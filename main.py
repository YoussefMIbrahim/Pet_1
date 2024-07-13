def main():

    print_header()
    print('hey')
    print_footer(2)
    
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
            pass
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



def print_footer(count):
    print(f"+{'-'*22}+")
    print(f"{count} rows in set.")

def print_header():
    
    print(f"+{'-'*22}+")
    print(f"| ID | Name      | AGE |")
    print(f"+{'-'*22}+")

    

main()