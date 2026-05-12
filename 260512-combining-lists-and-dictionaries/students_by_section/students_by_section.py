# A list of dictionaries (sections)
# so per dictionary, each represents a section
# and each section has two key-value pairs: 
#   1. name (string) 
#   2. students (a list of dictionaries or `list[dict]`)
#       so per dictionary in the students, represents a student
#       and each student has two key-value pairs:
#           1. first_name (stirng)
#           2. last_name (string)
students_by_section = [
    {
        "name": "1A",
        "students": [
            { "first_name": "Namjoon", "last_name": "Kim" },
            { "first_name": "Seokjin", "last_name": "Kim" },
            { "first_name": "Yoongi", "last_name": "Min" },
            { "first_name": "Hoseok", "last_name": "Jung" },
            { "first_name": "Jimin", "last_name": "Park" },
            { "first_name": "Taehyung", "last_name": "Kim" },
            { "first_name": "Jungkook", "last_name": "Jeon" },
        ]
    },
    {
        "name": "1B",
        "students": [
            { "first_name": "John Paulo ", "last_name": "Nase" },
            { "first_name": "Josh Cullen ", "last_name": "Santos" },
            { "first_name": "Stellvester ", "last_name": "Ajero" },
            { "first_name": "Felip John", "last_name": "Suson" },
            { "first_name": "Justin ", "last_name": "de Dios" },
        ]
    },
    {
        "name": "1C",
        "students": [
            { "first_name": "Jisoo", "last_name": "Kim" },
            { "first_name": "Jennie", "last_name": "Kim" },
            { "first_name": "Rosé", "last_name": "Park" },
            { "first_name": "Lisa", "last_name": "Manoban" },
        ]
    }
]