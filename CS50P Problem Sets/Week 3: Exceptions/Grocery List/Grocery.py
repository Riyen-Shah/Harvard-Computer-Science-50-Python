def Shopping():
    List = []
    while True:
        try:
            Item = input().upper()
        except EOFError:
            return List
        else:
            List.append(Item)

def duplicates():
    List = Shopping()
    Count = {}
    for Item in List:
        if Item in Count:
            Count[Item] += 1
        else:
            Count[Item] = 1
    return Count

List = duplicates()
for Item in sorted(List):
    print(f"{List[Item]} {Item}")
