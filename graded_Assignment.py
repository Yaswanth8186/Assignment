Question 1 - 

Description - Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 

Book - Introduction to Python Programming : Rs 499.00

Book - Python Libraries Cookbook : Rs. 855.00

Book - Data Science in Python : Rs. 645.00

Taxes and additional charges are described as details - 

GST : 12%

Delivery Charges : Rs. 250.00

code : 
  
book1_count = int(input("Enter the number of 'Introduction to Python Programming' books to be purchased(1 Unit cost = Rs 499.00) : "))
book2_count = int(input("Enter the number of 'Python Libraries Cookbook' books to be purchased(1 Unit cost = Rs 855.00) : "))
book3_count = int(input("Enter the number of 'Data Science in Python' books to be purchased(1 Unit cost = Rs 645.00) : "))
if(book1_count == 0 and book2_count == 0 and book3_count == 0):
    print("Please purchase any book")
elif(book1_count < 0 or book2_count < 0 or book3_count < 0):
    print("Enter valid number of books(zero or positive)")
else:
    book1_cost, book2_cost,book3_cost = 499.00,855.00,645.00
    book1_total, book2_total, book3_total = book1_cost * book1_count, book2_cost * book2_count, book3_cost * book3_count
    books_total = book1_total + book2_total + book3_total
    total_gst = books_total * 0.12
    delivery_charges = 250.00
    total_bill = books_total  + total_gst + delivery_charges
    print("Total Invoice : ",total_bill)

Question 2 -
        
Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.
    
code : 
  
string1 = input("Enter the String : ")
list1 = []
for i in string1.lower():
    if(i not in list1):
        list1.append(i)
print('Unique Letters are : ', end = '')
for i in range(len(list1)):
    if(i != len(list1) - 1):
        print(list1[i],end=',')
    else:
        print(list1[i])
        print('The number of unique letters are : ', len(list1))
