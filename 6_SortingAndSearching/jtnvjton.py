def analyzeAge( age ):
  if age < 21:
       print("You are a child")
  elif age >= 21: #Greater than or equal to
       print("You are an adult")
  else:   #Handle all cases where 'age' is negative 
       print("The age must be a positive integer!")

analyzeAge( 18 )  #Calling the function
list1 = [1,2,3,5,7,78]
print(list1[3::])