class obtain_triples:
    def alternative_triples(n):
        list_of_tuples=[]
        for i in range(1,n+1,1):
            for j in range(1,n+1,1):
                for k in range(1,n+1,1):
                    if i!=k and i!=j and k!=j:
                       tuple_=(i,j,k)
                       list_of_tuples.append(tuple_)
        return list_of_tuples
    
    def arrange_output(list_of_tuples):
        list_of_tuples.insert(0,(len(list_of_tuples), '', ''))
        df = pd.DataFrame(list_of_tuples, columns=['', '', ''])
        return print(df.to_string(index=False))
if __name__=="__main__":
    import pandas as pd
    n=3
    list_of_tuples=obtain_triples.alternative_triples(n)
    obtain_triples.arrange_output(list_of_tuples)
        


