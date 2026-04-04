rounds = [
    {
        'theme': 'Entrada',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
            'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
        }
    },
    {
        'theme': 'Plato principal',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
            'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
        }
    },
    {
        'theme': 'Postre',
        'scores': {
            'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
            'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
        }
    },
    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
            'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
            'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
        }
    },
    {
        'theme': 'Final libre',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
            'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
            'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
            'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
        }
    }
]

lista_nombres= list(rounds[0]['scores'])
lista_resultados= []

for p in range (len(rounds)):
	for j in range (len(rounds[p]['scores'])):
		puntos= list(rounds[p]['scores'][lista_nombres[j]].values())
		puntaje=0
		for i in range(3):
			puntaje+=puntos[i]
		
					

print(lista_resultados)
		
	
