import date_generator




def append_result_to_file(result, file_path):
    with open(file_path, 'a') as file:
        file.write(result + '\n')
    file.close()
    
n=date_generator.return_date()
append_result_to_file(f"{n}", 'result.txt')    

