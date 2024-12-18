

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

# Преобразовал списки словарей в датасет .csv c разделителем ",".
# Также для упрощения дальнейших рассчетов ввел в таблицу ещё один столбец "Taxed Salary (RUB)", в котором отобразились значения реальных зарплат по отделу после удержания налогов.
# Для анализа использовал два файла:
# corrected_employee_data.csv -  просто от зарплаты отнимается 13%
#updated_employee_data.csv - столбец Taxed Salary (RUB)=Salary (RUB)−(Salary (RUB)×(vat+hiring+sales)/100).


import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data = pd.read_csv("corrected_employee_data.csv")
print(data)
print()

#13. Вывести список отделов со средним налогом на сотрудников этого отдела.
def calculate_avg_tax(data):
    departments = data["Department"].unique()
    avg_tax_list = []

    for item in departments:
        dep_data = data[data["Department"] == item]
        avg_tax = (dep_data["Salary (RUB)"] - dep_data["Taxed Salary (RUB)"]).mean()
        avg_tax_list.append({"Department": item, "Avg Tax (RUB)": round(avg_tax, 2)})

    return pd.DataFrame(avg_tax_list)

avg_tax_df = calculate_avg_tax(data)
print(avg_tax_df)
print()

#14. Вывести список всех сотрудников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
employee_df = data[[
    "Department", "First Name", "Last Name", "Position", "Salary (RUB)", "Taxed Salary (RUB)"
]].copy()
employee_salaries = pd.DataFrame({
    "First Name": employee_df["First Name"],
    "Last Name": employee_df["Last Name"],
    "Зарплата 'на руки' (RUB)": employee_df["Taxed Salary (RUB)"]
})
print(employee_salaries)
print()


#15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
employee_df["Налоговая нагрузка"] = employee_df["Salary (RUB)"] - employee_df["Taxed Salary (RUB)"]
dep_tax_charge = employee_df.groupby("Department")["Налоговая нагрузка"].sum().reset_index()
dep_tax_charge = dep_tax_charge.sort_values(by="Налоговая нагрузка", ascending=False)
print(dep_tax_charge)
print()

#16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
employee_df = (data[[
    "First Name", "Last Name", "Salary (RUB)", "Taxed Salary (RUB)"
]].copy())

employee_df["Yearly Tax (RUB)"] = (employee_df["Salary (RUB)"] - employee_df["Taxed Salary (RUB)"]) * 12
employess_with_high_taxes = employee_df[employee_df["Yearly Tax (RUB)"] > 100000]
employees_names = employess_with_high_taxes[["First Name", "Last Name"]]
print("Список сотрудников с высокими годовыми налогами:")
print(employees_names)

#17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.

employee_df = (data[[
    "First Name", "Last Name", "Salary (RUB)", "Taxed Salary (RUB)"
]].copy())
employee_df["Yearly Tax (RUB)"] = (employee_df["Salary (RUB)"] - employee_df["Taxed Salary (RUB)"]) * 12
min_tax = employee_df["Yearly Tax (RUB)"].min()
min_tax_emp = employee_df[employee_df["Yearly Tax (RUB)"] == min_tax]
min_tax_emp_name = " ".join(min_tax_emp[["First Name", "Last Name"]].values[0]) # здесь попробовал преобразовать данные из датафрейма в массив, а затем в строку

print(f"Сотрудник с минимальной налоговой нагрузкой: {min_tax_emp_name}")
