import itertools
n=3
list_possible= list(range(1,n+1))
def possible(list_possible):
    list_of_tuples=[]
    list_of_tuples.extend(itertools.permutations(list_possible))
    return list_of_tuples
tuple_list=possible(list_possible)
tuple_list.insert(0,(len(tuple_list), '', ''))
import pandas as pd
df = pd.DataFrame(tuple_list, columns=['', '', ''])
print(df.to_string(index=False))
            
        


