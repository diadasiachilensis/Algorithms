class Alumno:
    def __init__(self):
        self.students = []

    def add_student(self,name,age):
        self.students.append({
            'Name': name,
            'age': age,
            'scores': []
        })

    def mean_score(self,name):
        for student in self.students:
            if student['Name'].lower() == name.lower():
                scores = student['scores']
                if len(scores) == 0:
                    print(f"⚠️ El estudiante {name} no tiene notas registradas.")
                    return None
                mean = sum(scores) / len(scores)
                print(f"📊 Promedio de {name}: {mean:.2f}")
                return mean
        print(f"❌ El estudiante {name} no está en la base de datos.")
        return None
    
    #funcion resumida
    """
    def mean_scores(self):
    return sum(self.students['scores']) / len(self.students['scores'])
    """

    def add_score(self,name,score):
        encontrado = False #Bandera
        for student in self.students:
            if student['Name'].lower() == name.lower():
                student['scores'].append(score)
                print(f"✅ Score {score} agregado a {student['Name']}")
                return
        print(f"❌ El estudiante {name} no está en la base de datos.")
    
    def show_all(self):
        print("\n📋 Lista de estudiantes:")
        for s in self.students:
            print(f"👤 {s['Name']} ({s['age']} años): {s['scores']}")

# Crear instancia
curso = Alumno()

# Agregar estudiantes
curso.add_student("Ana", 17)
curso.add_student("Pedro", 16)
curso.add_student("Lucas", 18)

# Agregar notas directamente
curso.add_score("Ana", 85)
curso.add_score("Ana", 90)
curso.add_score("Ana", 95)

curso.add_score("Pedro", 70)
curso.add_score("Pedro", 75)
curso.add_score("Pedro", 80)

curso.add_score("Lucas", 88)
curso.add_score("Lucas", 92)

# Mostrar información
curso.show_all()

# Calcular promedios individuales
curso.mean_score("Ana")
curso.mean_score("Pedro")
curso.mean_score("Lucas")