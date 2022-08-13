class Employee:
      def__init__(self,name,age,dob,city):
      #it is the local variable,so we convert into the variable
      self .name=name
      self.age=age
      self.dob=dob
      self.city=city
emp_1=Employee("gayu",21,2001,"theni")
emp_2=Employee("kalai",19,2003,"chennai")
print('name:',emp_1.name)
print('age:',emp_1.age)
print('dob:',emp_1.dob)
print('city:',emp_1.city)
print("******************")
print('name:',emp_2.name)
print('age:',emp_2.age)
print('dob:',emp_2.dob)
print('city:',emp_2.city)


OUTPUT:
      
 name:gayu
 
age:21
      
dob: 2001
      
 city:theni
      ******************
      
 name:kalai
      
 age:19
      
 dob:2003
      
 city:chennai    
