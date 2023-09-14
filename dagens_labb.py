def beräknar_årsinkomst_efter_skatt(månadslön):
    årsinkomst_brutto = månadslön*12
    SKATT_PÅ_450_000_31_PROCENT = 139500

    if årsinkomst_brutto <= 190_000:
        årsinkomst_netto = (årsinkomst_brutto*79)/100
    
    elif årsinkomst_brutto <= 450_000:
        årsinkomst_netto = (årsinkomst_brutto*69)/100
    
    else:
        skatt_på_över_450_000 = ((årsinkomst_brutto-450000)*56)/100
        årsinkomst_netto = årsinkomst_brutto - skatt_på_över_450_000 -SKATT_PÅ_450_000_31_PROCENT
    
    return årsinkomst_netto

månadslön = int(input('Skriv in din månadslön brutto: '))
årsinkomst = beräknar_årsinkomst_efter_skatt(månadslön=månadslön)
print(f"Min årsinkomst i år är {årsinkomst}!!!")