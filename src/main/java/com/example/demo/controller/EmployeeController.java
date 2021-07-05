package com.example.demo.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.entity.Employee;
import com.example.demo.service.EmployeeService;

@RestController
public class EmployeeController {

	@Autowired
	private EmployeeService ser;
	
	
	@PostMapping("/addemp")
	public Employee addemp(@RequestBody Employee e) {
		return ser.saveEmployee(e);
	}
	@GetMapping("/getallemp")
	public List<Employee> getallemp(){
		return ser.getEmployees();
	}
	@GetMapping("/getemp/{id}")
	public Employee getemp(@PathVariable int id) {
		return ser.getEmpbyID(id);
		
	}
	@DeleteMapping("/delete/{id}")
	public String delete(@PathVariable int id) {
		return ser.deletebyID(id);
	}
	
	@PostMapping("/update")
	public Employee update(@RequestBody Employee e) {
		return ser.updateEmployee(e);
	}
	
	@PostMapping("/addall")
	public List<Employee> addallemp(@RequestBody List<Employee> e) {
		return ser.saveall(e);
	}
}
