def beräkna_skatt(månadslön, skatt, svartarbete=0):
    """Månadslön i heltal och skatt i procent"""
    return (månadslön*skatt)/100 + svartarbete

print(beräkna_skatt(skatt=20, månadslön=25000))


