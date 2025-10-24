def filter_value(dictionary):
    passed={k:v for k,v in dictionary.items() if v >= 4.0}
    print("📘 Lista de estudiantes aprobados:\n")
    for key, value in passed.items():
        if value >= 6.0:
            emoji = "🏆"  # excelente
        elif value >= 5.0:
            emoji = "✅"  # aprobado
        else:
            emoji = "👍"  # suficiente
        
        print(f"{emoji} El estudiante {key} ha pasado con promedio {value:.1f}")
    
    print(f"\n🎓 Total de aprobados: {len(passed)} de {len(dictionary)} estudiantes ✅")
    return passed

students = {"Alice": 6.3, "Ben": 4.5, "Clara": 5.8, "David": 3.9, "Ella": 6.7, "Frank": 5.0, "Grace": 4.2, "Henry": 6.1, "Ivy": 5.5, "Jack": 3.7, "Kelly": 6.8, "Leo": 4.8, "Mia": 6.0, "Noah": 5.2, "Olivia": 4.9}
filter_value(students)