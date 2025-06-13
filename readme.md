# 🚀 Object-Oriented Programming (OOP) in Python

This repository explains the basic concept of **Object-Oriented Programming (OOP)** using Python, focusing on **Classes**, **Objects**, and the difference between **Class Attributes** and **Instance Attributes**.

---

## 📚 What You Will Learn:

- ✔️ What is a **Class**?
- ✔️ How to create **Objects**?
- ✔️ Difference between **Class Attributes** and **Instance Attributes**.
- ✔️ Real-life example of **Employee Class**.

---

## 🔍 Example Code Overview:

### 👨‍💼 Employee Class Example:

```python
class Employee:
    country = "Pakistan"  # Class Attribute
    salary = 1200000      # Class Attribute

# Creating Objects
employee1 = Employee()
employee1.name = 'Nabeel'  # Instance Attribute
print(employee1.country, employee1.salary)

employee2 = Employee()
employee2.name = 'Ali'     # Instance Attribute
print(employee2.country, employee2.salary)
