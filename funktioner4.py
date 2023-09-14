def funktionsväljare(val):
    def jämnt():
        print('jämnt')
    def udda():
        print('udda')

    return jämnt if val == 0 else udda

min_funktion = funktionsväljare(1)

min_funktion()
print(min_funktion)