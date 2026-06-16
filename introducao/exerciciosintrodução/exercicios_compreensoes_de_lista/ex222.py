transitions = [250.0, -30.0, 0, 520.99, -5.0, 89.90, 1200.0, -0.01, 75.0]
transforming_data = [round(value * 5.70,2) for value in transitions if value > 0]
print(transforming_data)