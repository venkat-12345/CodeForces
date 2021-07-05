package com.example.demo.entity;




import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="Employee")
public class Employee {
	
	@Id
	@GeneratedValue
	private int id;
	private String name;
	private double salary;
	private String field;


	public String getField() {
		return field;
	}
	public void setField(String field) {
		this.field = field;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getSalary() {
		return salary;
	}
	public void setSalary(double salary) {
		this.salary = salary;
	}

	public Employee(int id, String name, double salary, String field) {
		super();
		this.id = id;
		this.name = name;
		this.salary = salary;
		
		this.field = field;
	}
	public Employee() {
		super();
		// TODO Auto-generated constructor stub
	}
	
	
}
