
try:
    Alice_grade = float(input("\nEnter the grade Alice received: "))
    Guy_grade = float(input("\nEnter the grade Guy received: "))

    print("\nTheir average grade is", ((Alice_grade + Guy_grade) / 2),"\n")

except ValueError:
    print("\nInvalid Data Input for float\n")