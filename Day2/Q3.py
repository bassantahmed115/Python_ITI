def convert_names_to_sorted_dict():

        name_list = input("Enter a list of names separated by commas: ").split(",")
        name_list = [name.strip() for name in name_list]
        
        sorted_dict = {}
        for name in name_list:
            if name[0].isalpha():
                first_letter = name[0].upper()
                if first_letter in sorted_dict:
                    sorted_dict[first_letter].append(name)
                else:
                    sorted_dict[first_letter] = [name]
        
        for key, value in sorted(sorted_dict.items()):
            print(f"{key}: {value}")
    
convert_names_to_sorted_dict()
