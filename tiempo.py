def seg_min(seg):
    return seg /60

def min_hrs(min):
    return min /60

if __name__ == "__main__":
    seg =150
    min = seg_min(seg)
    print (f"{seg} segundos son equivalentes a{min} minutos")