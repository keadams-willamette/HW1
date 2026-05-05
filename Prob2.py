import json

"""def get_data(filename):
    """Retrieves the parsed JSON data from the given filename"""
    with open (filename) as fh:
        data=json.load(fh)
    bookcount=0
    for item in data["books"]:
        bookcount+=1
    print(bookcount, "books" )
    total_langauges=[]
    booktracker=0
    j=2026
    for i in range(bookcount):
        if data["books"][i].get("first_publish_year")!= None:
            if data["books"][i]["first_publish_year"]<j:
                j=data["books"][i]["first_publish_year"]
                booktracker=i
    print( data["books"][booktracker]["title"], j)
    for i in range(bookcount):
        if data["books"][i].get("language")!= None:
            for x in data["books"][i]["language"]:
                if x not in total_langauges:
                    total_langauges.append(x)
    print("There are",len(total_langauges), "total unique langauges:", total_langauges)
    pure_sanderson=[]
    for i in range(bookcount):
        if len(data["books"][i].get("author_name", 0))==1:
            pure_sanderson.append(data["books"][i])
    with open ("pure_sanderson.json", "w") as fh:
        json.dump(pure_sanderson,fh, indent=2)"""
   
        
blank_list=[]


            



if __name__ == '__main__':
    #data = get_data('sanderson.json')
    
