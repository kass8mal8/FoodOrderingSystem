""" Design a food ordering system where your python program will run two threads.
    1.Place order : This thread will be placing an order and inserting that into a queue.This thread places new order every 0.5s
    2.Serve order : This thread will serve the order.All you need to do is pop the order out of the queue and print it.This thread serves an order every 2s."""

import time
import os
    
class Queue :
    def __init__(self):
        self.orders = []
        self.size = 0
    
    def enqueue (self,data) :
        new = self.orders.append(data)
        self.size += 1
        
        return new
    
    def dequeue (self) :
        order = self.orders.pop(0)
        self.size -= 1
        
        return order
    
class Food :
    def __init__(self,title = None) :
        self.title = title
        
class OrderSystem (Queue) :
    def __init__(self):
        super().__init__()
        
    def placeOrder (self,order) :
        self.enqueue(order)
                
    def serveOrder (self) :
        quantity = 0
        
        while self.size > 0 :
            current_order = self.dequeue()
            print(f"Current order: {current_order.title} ")
            quantity += 1
            time.sleep(2)
            
            if self.size == 0 :
                print(f"All {quantity} orders served... Welcome")
            
ordersystem = OrderSystem ()

""" 
    Open orders file and pass the values to the class
    """
        
os.chdir('FoodOrderingSystem/')   
orders = [line.strip() for line in open('orders.txt')]

print("-"*4 ," Hotel ordering system ", "-"*4,"\nFetching orders ...")


for order in orders :
    food = Food (order)
    ordersystem.placeOrder(food)
        
ordersystem.serveOrder()