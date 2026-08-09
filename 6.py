basic_salary= float(input("enter your user salary"))
allowance=basic_salary * 0.15
tax=(basic_salary + allowance) * 0.10
net_salary=basic_salary + allowance - tax
print("tax:" ,round(tax,2))
print("allowance:" ,round(allowance,2))
print("ner_salary:" ,round(net_salary,2))



