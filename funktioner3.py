talet = 2
def undersök_tal(tal):

    def udda(nummer, anropa_jämnt = False):
        tal = 42
        print(f"Talet tal är {tal} men nummer är {nummer} och talet är {talet}!")

        def jämnt(nummer):
            print(f"Talet {tal} är jämnt ocn nummer är {nummer}!")   
        if anropa_jämnt:
            jämnt(nummer=nummer)

    if tal%2==0:
        udda(tal**2, anropa_jämnt=True)
    else:
        udda(tal**2)

    print(tal)
undersök_tal(2)
