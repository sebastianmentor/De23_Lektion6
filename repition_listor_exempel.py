# print([1,2,3] in [[1,2,3],1,2,3,4,5] )

# lista_djur =  ['häst', 'ko', 'katt']
favorit_djur =  ['häst', 'ko', 'katt']

något_djur_har_stor_bokstav = False
# for djur in lista_djur:
#     djurets_första_bokstav = djur[0]
#     djurets_första_bokstav_stor_bokstav = djur[0].upper()

#     if djurets_första_bokstav == djurets_första_bokstav_stor_bokstav:
#         något_djur_har_stor_bokstav
#         break
# lista_med_sanningen = []
# for djur in lista_djur:
#     if djur[0] == djur[0].upper():
#         lista_med_sanningen.append(True)
#     else:
#         lista_med_sanningen.append(False)

# print(lista_med_sanningen)
# print(all(lista_med_sanningen))
# print(any(lista_med_sanningen))
lista_med_djur = []
while True:
    print("1. Lägg till djur\n2. Avsluta")
    val = input('>>>>')
    if val == '1':
        djur = input('Skriv in ett djur: ').lower()
        if not (djur in lista_med_djur):
            lista_med_djur.append(djur)
        else:
            print('Djuret finns redan i listan!')

    elif val == '2':
        break
    else:
        print('Error')

antal_djur_vi_gillar_tillsammans = 0
for användarens_djur in lista_med_djur:
    if användarens_djur in favorit_djur:
        antal_djur_vi_gillar_tillsammans += 1


