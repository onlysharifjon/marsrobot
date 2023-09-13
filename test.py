bolakaylar = [
    ['Dias Djumabayev', 642181, '90-988-46-73', 0],
    ['Mansur Muxtorov', 457658, '97-494-46-36', 0],
    ['Bekzod Xotamov', 335935, '97-115-53-00', 0],
    ['Maqsud Odilxo`jayev', 564850, '93-070-46-16', 0],
    ['Javoxir Maqsudov', 359725, '99-852-6943', 0],
    ['Maryambonu Mirzayeva', 336845, '90-321-8003', 1],
]


print(bolakaylar[4][2])
id = int(input('modme ID ni kiriting: '))
count = 0
for i in bolakaylar:
    count+=1
    if i[1] == id:
        print(count)
        print(i[0])


