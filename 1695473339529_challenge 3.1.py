def linearsearchproduct(productList, targetproduct):
    indices=[]

    for index, product in enumerate(productList):
         if product==targetproduct:
              indices. append(index)

    return indices



#Example usage
products=["shoes","boot","leofer","shoes","sandal","shoes"] 
target="shoes"
target2='apple'
result=linearsearchproduct(products, target)
print(result)
result1=linearsearchproduct(products,target2)
print(result)