import random
from typing import List, Union, Tuple

def generate_data(N: int, num_dormitories: int, num_departments: int) -> Tuple[
    List[int], List[Union[0, 1, 2, 3]], List[List[int]], List[int],
    List[int], List[Tuple[float, float]], List[Tuple[float, float]]
]:
    # Students data
    students_years = [random.randint(1, 5) for _ in range(N)]  # Losowy rok studiów od 1 do 5
    students_disability = random.choices([0, 1, 2, 3], weights=[70, 15, 10, 5], k=N) # Stopień niepełnosprawności
    students_priority_lists = [random.sample(range(num_dormitories), num_dormitories) for _ in range(N)]  # Priorytety akademików
    students_departments = [random.randint(0, num_departments - 1) for _ in range(N)]  # Losowy wydział dla każdego studenta
    student_sex = random.choices([0, 1], weights=[35, 65], k=N)

    # Dormitories data
    dormitory_position = []
    dormitorys_capacity = []
    for y in range(num_dormitories):
        dormitory_position.append((round(random.uniform(1, 50), 2), round(random.uniform(1, 50), 2)))  # Losowa pozycja akademika (x, y)
        
    for y in range(num_dormitories):
        dormitorys_capacity.append(random.randint(50, 200))  # Losowa pojemność akademika


    # Departments data
    departments_position = []
    for y in range(num_departments):
        departments_position.append((round(random.uniform(1, 50), 2), round(random.uniform(1, 50), 2)))

    return (
        students_years,
        students_disability,
        students_priority_lists,
        students_departments,
        student_sex,
        dormitorys_capacity,
        dormitory_position,
        departments_position
    )