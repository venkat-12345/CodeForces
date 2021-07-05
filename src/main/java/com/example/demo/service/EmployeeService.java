package com.example.demo.service;

import java.util.List;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.entity.Employee;
import com.example.demo.repository.EmployeeRepository;

@Service
public class EmployeeService {

	@Autowired
	private EmployeeRepository rep;
	
	public Employee saveEmployee(Employee e) {
		
		return rep.save(e);
	}
	public List<Employee> getEmployees(){
		return rep.findAll();
	}
	public Employee getEmpbyID(int id) {
		return rep.findById(id).orElse(null);
	}
	public String deletebyID(int id) {
		rep.deleteById(id);
		return "Employee of"+id+"is successfully deleted";
	}
	public Employee updateEmployee(Employee e) {
		int n=e.getId();
		rep.deleteById(n);
		return rep.save(e);
	}
	public List<Employee> saveall(List<Employee> e){
		return rep.saveAll(e);
	}

	
	
}
