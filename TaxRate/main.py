#Title: Tax Rate
#Author: Dominic Corneliusen
#Date last modified: 2/27/2026

#Start
def tax(Sales):
    countyTax = round(Sales * 0.025, 2)
    stateTax = round(Sales * 0.05, 2)
    totalSalesTax = round(countyTax + stateTax, 2)
    print("County tax is:", countyTax )
    print("State tax is:", stateTax)
    print("Total sales tax is:", totalSalesTax)
tax(int(input("Enter the total sales tax: ")))