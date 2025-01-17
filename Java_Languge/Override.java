class Employee {
    public void work() {
        System.out.println("Employee is working.");
    }

    public double getSalary() {
        return 50000.0;
    }
}

class HRManager extends Employee {
    @Override
    public void work() {
        System.out.println("HR Manager is managing HR tasks.");
    }

    public void addEmployee() {
        System.out.println("HR Manager is adding a new employee.");
    }
}

public class Main {
    public static void main(String[] args) {
        Employee emp1 = new Employee();
        HRManager hrManager = new HRManager();

        emp1.work();
        System.out.println("Employee Salary: $" + emp1.getSalary());

        hrManager.work();
        hrManager.addEmployee();
    }
}


//output
//Employee is working.
//Employee Salary: $50000.0
//HR Manager is managing HR tasks.
//HR Manager is adding a new employee.
