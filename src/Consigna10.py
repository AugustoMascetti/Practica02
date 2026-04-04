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
aux_tematica= 0
lista_nombres= list(rounds[0]['scores'])
lista_resultados= []
contador_victorias= {
	'Valentina': 0,
	'Mateo':0,
	'Camila':0,
	'Santiago':0,
	'Lucía':0
	}
for r in range (len(lista_nombres)):
	lista_resultados.append([lista_nombres[r]])

for p in range (len(rounds)):
	for j in range (len(rounds[p]['scores'])):
		puntos= list(rounds[p]['scores'][lista_nombres[j]].values())
		puntaje=0
		for i in range(3):
			puntaje+=puntos[i]
		lista_resultados[j].append(puntaje)

for f in range(1,len(rounds)+1):
	lista_resultados.sort(key=lambda x: x[f], reverse=True)
	
	contador_victorias[lista_resultados[0][0]] += 1
	print(f'''
	    Ronda {f} -{rounds[aux_tematica]['theme']}
		Ganador: {lista_resultados[0][0]:<12}       ({lista_resultados[0][f]})
		Segundo lugar: {lista_resultados[1][0]:<12} ({lista_resultados[1][f]})
		Tercer lugar: {lista_resultados[2][0]:<12}  ({lista_resultados[2][f]})
		Cuarto lugar: {lista_resultados[3][0]:<12}  ({lista_resultados[3][f]})
		Quinto lugar: {lista_resultados[4][0]:<12}  ({lista_resultados[4][f]})
		''')
	aux_tematica +=1
	print('-------------------------------------------------------------------------------------')
	print()
print('''
''')