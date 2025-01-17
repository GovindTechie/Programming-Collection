class Employee {
    String name;
    String address;
    double salary;
    String jobTitle;
    public Employee(String name, String address, double salary, String jobTitle) {
        this.name = name;
        this.address = address;
        this.salary = salary;
        this.jobTitle = jobTitle;
    }
    public double calculateBonus() {
        return 0.0;
    }
    public String generatePerformanceReport() {
        return "Performance report for " + name;
    }
}
class Manager extends Employee {
    public Manager(String name, String address, double salary) {
        super(name, address, salary, "Manager");
    }
    @Override
    public double calculateBonus() {
        // Implement bonus calculation for managers
        return salary * 0.1;
    }
    public void manageProjects() {
        // Implement project management logic
    }
}
class Developer extends Employee {
    public Developer(String name, String address, double salary) {
        super(name, address, salary, "Developer");
    }
    @Override
    public double calculateBonus() {
        return salary * 0.05;
    }
}
class Programmer extends Employee {
    public Programmer(String name, String address, double salary) {
        super(name, address, salary, "Programmer");
    }
    @Override
    public double calculateBonus() {
        return salary * 0.03;
    }
}
public class Main {
    public static void main(String[] args) {
        Manager manager = new Manager("John Doe", "123 Main St", 60000.0);
        Developer developer = new Developer("Alice Smith", "456 Elm St", 50000.0);
        Programmer programmer = new Programmer("Bob Johnson", "789 Oak St", 45000.0);
        System.out.println("Manager's Bonus: $" + manager.calculateBonus());
        System.out.println("Developer's Bonus: $" + developer.calculateBonus());
        System.out.println("Programmer's Bonus: $" + programmer.calculateBonus());
        manager.manageProjects(); 
        String managerReport = manager.generatePerformanceReport();
        System.out.println(managerReport);
    }
}

//Output