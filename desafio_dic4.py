"""
Exercício 4 — Notas de alunos 

Crie um dicionário onde as chaves são nomes de alunos e os valores são listas de notas. Mostre a média de cada aluno. 

python 

alunos = { 
   "Ana": [7, 8, 9], 
   "João": [5, 6, 5], 
   "Maria": [9, 9, 10] 
} 
# Ana: 8.0 
# João: 5.3 
# Maria: 9.3 

"""
alunos = { 
   "Ana": [7, 8, 9], 
   "João": [5, 6, 5], 
   "Maria": [9, 9, 10] 
}
def media_notas(alunos):
    for nome, notas in alunos.items():
      media = sum(notas) / len(notas)
      print(f"{nome}: {media:.1f}")
print(media_notas(alunos))

  
