def kg_g(kg):
    return kg *1000

def kg_t(kg):
    return kg /1000

if __name__ == "__main__":
    mikg = 2.5
    gram = kg_g(mikg)
    print(f"{mikg} kilogramos son {gram} gramos")