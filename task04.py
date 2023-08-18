# Задача 4: Поиск уникальных элементов в списке. Напишите программу, которая создает новый список, содержащий только уникальные элементы из исходного списка.

def unic_elements(list):
    unic_list = []
    
    for element in set(list):
        unic_list.append(element)
        
    return(unic_list)


spisok = [1,2,1,3,5,2,"a","d","a","d","das","ds",]
print(f"Список уникальных элментов = {unic_elements(spisok)} из списка {spisok}")
