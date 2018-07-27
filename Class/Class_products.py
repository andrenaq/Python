# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 21:21:48 2018

@author: andre
"""

class products(object):
        def __init__(self,name,price,discountpercent):
            self.name = name
            self.price = price
            self.discountpercent = discountpercent
        def getDiscountAmount(self):
            return self.price*self.discountpercent
        def getDiscountprice(self):
            return (self.price - self.getDiscountAmount())

def main():
    product1 = products("Led Tv",1245,.10)
    print("The product is a {} and it costs ${:.2f}. ".format(product1.name,(product1.price )))
    print("The available discout is {}%, or ${}".format(100*product1.discountpercent, product1.getDiscountAmount()))
    print("The final prince is ${:.2f}".format(product1.getDiscountprice()))
    
if __name__ == "__main__": 
    main()
