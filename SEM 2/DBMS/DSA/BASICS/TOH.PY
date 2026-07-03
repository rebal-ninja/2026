def TOH(n,source,auxillary,destination): 
    if n==0: 
        return 
    else: 
        TOH(n-1,source,destination,auxillary) 
        print(f"move disk {n} from {source}to{destination}") 
        TOH(n-1,auxillary,source,destination) 
n=3 
TOH(n,'A','B','C') 