import application.salary as sal
import application.db.people as emp
import current_date as cd


if __name__ == '__main__':
    sal.calculate_salary()
    emp.get_employees()
    cd.cd()