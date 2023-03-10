import __future__
import sys
import json
from random import randint

def main():
    minT = sys.argv[1]
    maxT = sys.argv[2]
    minT = int(minT)
    maxT = int(maxT)
    values = range(minT,maxT)
    #print("começo")
    for z in values:
        #print("z==",z)
        UTILIZACAO_ALVO = int(z)
        utilizacao_atual = 0
        #print("ALVO",UTILIZACAO_ALVO)
        #print(utilizacao_atual)
        
        min_parcelas = (UTILIZACAO_ALVO/10) + 1
        max_parcelas = (UTILIZACAO_ALVO/5) + 1
        #print(min_parcelas)
        #print(max_parcelas)
        min_parcelas = int(min_parcelas)
        #print(min_parcelas)
        max_parcelas = int(max_parcelas)
        #print(max_parcelas)

        #RandomTasksGenerator/data

        num_parcelas = randint(min_parcelas,max_parcelas)
        
        utilizacao_atual = 0
            
        min_valor_parcela = 0
        max_valor_parcela = 0

        parcelas = []
        parcelasSuperiores = []
        
        for i in range(0, num_parcelas):
            min_valor_parcela = int((UTILIZACAO_ALVO-utilizacao_atual)/20) + 1

            max_valor_parcela = int((UTILIZACAO_ALVO-utilizacao_atual)/5) + 1

            
            #print ("min parcela", minT)
            #print ("max parcela", maxT)
            parcela = randint(min_valor_parcela,max_valor_parcela)

            utilizacao_atual += parcela
            
            parcelas.append(parcela)
            #print(parcela)
        
        parcelas[-1] = parcelas[-1] + (UTILIZACAO_ALVO - utilizacao_atual)

        #print("---")
        for i in range(0,num_parcelas):
            aux = parcelas[i] 
            parcelas[i] = parcelas[i] * 100
            parcelasSuperiores.append((aux * UTILIZACAO_ALVO)/num_parcelas)
            #print(parcelasSuperiores[i])
        #print("final-----------")

        #for i in range(0,num_parcelas):
            #print(parcelasSuperiores[i],"/",parcelas[i])
            
        filename = f'RandomTasksGenerator/data/{z}.json'
        arqOutJson = {
                'Processos':{

                }
            }

        for i in range(0,num_parcelas):
            arqOutJson['Processos'][f'processo{i+1}'] = [parcelasSuperiores[i],parcelas[i]]
        

        with open (filename,"w") as outfile:
            json.dump(arqOutJson,outfile,indent=4)
            

if __name__ == "__main__":
    main()




