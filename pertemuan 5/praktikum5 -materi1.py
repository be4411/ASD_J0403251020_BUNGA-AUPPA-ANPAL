#==========================================================
#Nama : Bunga Auppa Anpal
#NIM : J0403251020
#Kelas : TPL-B2
#==========================================================

#==========================================================
#materi rekursif : faktorial
# 3! = 3 x 2 x 1 base case
# base case => berhenti
#===========================================================

def faktorial(n):
    #base case
    if n == 0:
        return 1


    #rekursif case
    return n*faktorial(n-1)  #n-1*n-2*n-3 bla bla blap
print("=====program faktorial======")
print ("hasil faktorial : ", faktorial(10))


