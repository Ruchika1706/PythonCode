height = float(raw_input("Enter you Height in meters"))
weight = float(raw_input("Enter you Weight in Kgs"))
def calculate_BMI(height, weight):
    BMI = weight/((height)**2)
    print(BMI)
calculate_BMI(height,weight)