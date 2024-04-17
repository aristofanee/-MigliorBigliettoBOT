import make_request
import json
import datetime

def main():
        
    with open("user_request.json", "r") as file:
            user_requests = json.load(file)

    best_offers = []

    for userRequest in user_requests["searchObjects"]:
            
            for research in userRequest["searchParameters"]:
                    city_in = research["departureCity"]
                    city_out = research["arrivalCity"]
                    days_to_check = 1 #research["searchPeriod"]
                    prezzo_soglia = research["prezzoSoglia"]

                    for ore in range(days_to_check*24):

                        print("il giorno va avanti")

                            
                        request_output = json.loads(make_request.create_request(city_in, city_out, 1000, 0, ore))
                        best_offers = find_best_solution(best_offers, request_output, prezzo_soglia)

    print(best_offers)


                
        

def find_best_solution(best_offers, request, soglia):

    
       
    for solutions in request["solutions"]:

        skip_solution = False

        print("le soluzioni sono: ", len(solutions))


        if solutions["solution"]["price"] == None:
            print("porcaccio dio non c'è il prezzo")
            continue

        prezzo_soluzione = solutions["solution"]["price"]['amount']
        id_soluzione = solutions["solution"]["id"]


        print(prezzo_soluzione)

        for offerte_salvate in best_offers:
        
            if not best_offers:
                continue

            elif (id_soluzione == offerte_salvate["solutionID"]) or (prezzo_soluzione > offerte_salvate["prezzo"]):
                skip_solution = True
                continue
            elif prezzo_soluzione < offerte_salvate["prezzo"] and prezzo_soluzione > soglia:
                best_offers = []


        

        if skip_solution:
            continue
        else:
            best_offers.append(
            {
                "solutionID": id_soluzione,
                "stazioneIn": solutions["solution"]["origin"],
                "stazioneOut": solutions["solution"]["destination"],
                "numeroCambi": len(solutions["solution"]["nodes"]),
                "dataEora": solutions["solution"]["departureTime"],
                "prezzo": prezzo_soluzione
            }
            )

    print_offers(best_offers)    
    return best_offers





def print_offers(list_offers):
    print("\n\n----------------------------------------------------\n")
    print("\nSono state trovate ", len(list_offers), "offerte:\n")
    

    for offerta in list_offers:
        
        data = datetime.datetime.fromisoformat(offerta["dataEora"])

        
        print(data)
        print("Da ", offerta["stazioneIn"], " a ", offerta["stazioneOut"], end = "")
        print(", facendo", offerta["numeroCambi"], "cambi")
        print("Prezzo: ", offerta["prezzo"])
        
         
            

main()