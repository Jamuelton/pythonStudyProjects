question_1 = input("Olá, você quer comprar comida ou vender comida?")

if question_1 == 'comprar':
    name = input("qual o nome do seu estabelecimento?")
    restaurants = []
    restaurants.append(name)
    restaurants = enumerate(restaurants)
    print(restaurants)
    
    