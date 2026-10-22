schools = ["NAHPI", "COLTECH", "HICM", "HITL", "HTTC"]
# houses = ["Nyah", "Ngam", "Chiaboh", "Ning", "Bolam"]

houses = {
    "Nyah":"Sabastine",
    "Ngam":"Godlove",
    "Bih":"Nayah"
}

students = [
    {"name":"Sabastine","house":"Nyah","course":"CompEng"},
    {"name":"Juliette","house":"Nyah","course":"Accounting"},
    {"name":"Quinette","house":"Nyah","course":"TeachersTraining"},
    {"name":"Georgianna","house":"Nyah","course":"Doctor"},
]

for student in students:
    print(student["name"], student["house"], student["course"], sep=", ")

'''
for house in houses:
    print(house) #prints just the keys Nyah, Ngam and Bih
    print(house,houses[house])

'''
# for school in schools:
#     print(school)

# for i in range(len(schools)):
#     print(i+1,schools[i], sep=': ')


 
