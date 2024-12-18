

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

def dep_names_output (departments): # 1. Вывести названия всех отделов
    dep_names = []
    for item in departments:
        dep_name = item["title"]
        dep_names.append(dep_name)
    return dep_names
all_dep_names = dep_names_output(departments)
str_all_d_n = "\n".join(all_dep_names)
print(str_all_d_n)
print()


def employers_names_output (departments): #2. Вывести имена всех сотрудников компании.
    all_employers_names = []
    for item in departments:
        for employer in item["employers"]:
            employer_name = employer['first_name'] + " " + employer['last_name']
            all_employers_names.append(employer_name)
    return all_employers_names
all_employers_names = employers_names_output(departments)
str_all_e_n = "\n".join(all_employers_names)
print(str_all_e_n)
print()

def dep_employers_names(departements): # 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
    for item in departements:
        print(item["title"])
        for employer in item["employers"]:
            print(f"{employer['first_name']} {employer['last_name']}")
        print()
all_dep_emp_names = dep_employers_names(departments)

def dep_employers_names2(departements):# 3. Вывел имена всех сотрудников компании с указанием отдела, в котором они работают через возвращение функции
    result = []
    for item in departements:
        result.append(item['title'])
        for employer in item["employers"]:
            result.append(f"{employer['first_name']} {employer['last_name']}")
    return result
dep_emp_n = dep_employers_names2(departments)
print("\n".join(dep_emp_n))
print()




def emp_names_biggest_salary (departments): # 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
    emp_with_biggest_salary = []
    for item in departments:
        for employer in item["employers"]:
            if employer["salary_rub"]>= 100000:
                full_name = f"{employer['first_name']} {employer['last_name']}"
                emp_with_biggest_salary.append(full_name)
    return emp_with_biggest_salary
print("Сотрудники с самой высокой зарплатой:")
result = emp_names_biggest_salary(departments)
result_str = "\n".join(result)
print(result_str)
print()

def poor_position (departments): # 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
    bad_position = []
    for item in departments:
        for employer in item["employers"]:
            if employer["salary_rub"]<80000:
                position = f"{employer['position']}"
                bad_position.append(position)
    return bad_position
print("Позиции с самой низкой зарплатой:")
result = poor_position(departments)
unique_result = list(set(result))
result_str = "\n".join(unique_result)
print(result_str)
print()

def dep_costs_per_month (departments): # 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела.
    dep_costs = {}
    for item in departments:
        total_salary = 0
        for employer in item["employers"]:
            total_salary += employer["salary_rub"]
        dep_costs[item["title"]] = total_salary
    return dep_costs
dep_total_salary = dep_costs_per_month(departments)
for department, total in dep_total_salary.items(): # Долго не мог понять, как вывести словарь в виде строки. В итоге GPT подсказал метод items для распаковки словаря. Так можно?
    print(f"В месяц уходит на {department}: {total} рублей")
print()


def min_salary_by_dep (departments): #7 Вывести названия отделов с указанием минимальной зарплаты в нём
    salaries = []
    for item in departments:
        for employer in item["employers"]:
            salaries.append(employer["salary_rub"])
        min_salary = min(salaries)
        print(f"Минимальная зарплата в {item['title']}: {min_salary}")
minimorum = min_salary_by_dep(departments)
print(minimorum)
print()


def min_max_avg_salary_by_dep(departments): #8.Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
    salaries = []
    for item in departments:
        for employer in item["employers"]:
            salaries.append(employer["salary_rub"])
        if len(salaries) > 0:
            min_salary = min(salaries)
            max_salary = max(salaries)
            avg_salary = sum(salaries) / len(salaries)
            print(f"Средняя зарплата в отделе {item['title']}: {avg_salary} рублей")
            print(f"Максимальная зарплата в отделе {item['title']}: {max_salary} рублей")
            print(f"Минимальная зарплата в отделе {item['title']}: {min_salary} рублей")
        else:
            print(f"В отделе {item['title']} зарплату не платят")
    return
all_types_of_salaries = min_max_avg_salary_by_dep(departments)
print()


def total_avg_salary (departements): #9. Вывести среднюю зарплату по всей компании.
    total_salary = 0
    total_employers = 0
    for item in departements:
        for employer in item["employers"]:
            total_salary += employer["salary_rub"]
            total_employers += 1
        if total_employers > 0:
            return total_salary / total_employers
        else:
            print("В этой компании нет либо работников, либо зарплат")

avd_salary_by_company = total_avg_salary(departments)
print(f"Средняя зрплата по компании: {avd_salary_by_company}")
print()

def good_position (departments): #10. Вывести названия должностей, которые получают больше 90к без повторений.
    good_position = []
    for item in departments:
        for employer in item["employers"]:
            if employer["salary_rub"] > 90000:
                position = f"{employer['position']}"
                good_position.append(position)
    return good_position

print("Позиции с зарплатой выше 90000:")
result = good_position(departments)
unique_result = list(set(result))
result_str = "\n".join(unique_result)
print(result_str)
print()


def avg_girls_salary (departments): #11 Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
    total_girls_salary = 0
    total_girls_num = 0
    for item in departments:
        for employer in item["employers"]:
            if employer["first_name"] == "Michelle" or "Nicole" or "Caitlin" or "Christina":
                total_girls_salary += employer["salary_rub"]
                total_girls_num += 1
    if total_girls_num > 0:
        avg_girls_salary = total_girls_salary / total_girls_num
        return avg_girls_salary
avg_g_s = avg_girls_salary(departments)
print(f"Средняя зарплата по девочкам каомпании: {avg_g_s}")
print()

def unique_names_with_vowels (departments): #12
    unique_names = set()
    vowels = "aeiouAEIOU"
    for item in departments:
        for employer in item["employers"]:
            first_name = employer["first_name"]
            if first_name[-1] in vowels:
                unique_names.add(first_name)
    return "\n".join(sorted(unique_names))

name_list = unique_names_with_vowels(departments)
print(f"Список имён, заканчивающихся на гласную: {name_list}")













