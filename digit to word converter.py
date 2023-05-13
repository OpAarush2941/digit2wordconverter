from tkinter import *
root = Tk()
    
root.geometry("600x400")
root.title("Digit To Word Converter")
   
Label1=Label(root, text="Digit To Word Converter")
Label1.place(relx=0.5, rely=0.2, anchor=CENTER)
    
label2=Label(root, text="Number: ")
label2.place(relx=0.4, rely=0.4, anchor=CENTER)
    
num=Entry(root)
num.place(relx=0.6, rely=0.4, anchor=CENTER)
    
ans=Label(root)
ans.place(relx=0.5, rely=0.6, anchor=CENTER)

once_text = ""
tens_text = ""
hundred_text = ""
thousand_text = ""
Tthousand_text = ""
Lakh_text = ""
Tlakh_text = ""
Crore_text = ""

    
def convertion():
    global ones_text
    global tens_text
    global hundred_text
    global thousand_text
    global Tthousand_text
    global Lakh_text
    global Tlakh_text
    global Crore_text
    
    
    number = int(num.get())
    ones = number % 10
    tens = (number % 100)//10
    hundred = (number % 1000)//100
    thousand = (number % 10000)//1000
    Tthousand = (number % 100000)//10000
    Lakh = (number % 1000000)//100000
    Tlakh = (number % 10000000)//1000000
    Crore = (number % 100000000) // 10000000
    
    
    if ones == 1:
        ones_text = "one"
    
    if ones == 2:
    	ones_text = "two"
    
    if ones == 3:
    	ones_text = "three"
    
    if ones == 4:
    	ones_text = "four"
    	
    if ones == 5:
    	ones_text = "five"
    
    if ones == 6:
    	ones_text = "six"
    
    if ones == 7:
    	ones_text = "seven"
        
    if ones == 8:
    	ones_text = "eight"
    
    if ones == 9:
    	ones_text = "nine"
        
    if ones == 0:
        ones_text = ""
        
    if (tens == 1) and (ones == 1) :
        tens_text = "eleven"
        ones_text = ""
        
    if (tens == 1) and (ones == 2) :
        tens_text = "twelve"
        ones_text = ""
        
    if (tens == 1) and (ones == 3) :
        tens_text = "thirteen"
        ones_text = ""
        
        
    if (tens == 1) and (ones == 4) :
        tens_text = "fourteen"
        ones_text = ""
        
    if (tens == 1) and (ones == 5) :
        tens_text = "fifteen"
        ones_text = ""
        
    if (tens == 1) and (ones == 6) :
        tens_text = "sixteen"
        ones_text = ""
    
    if (tens == 1) and (ones == 7) :
        tens_text = "seventeen"
        ones_text = ""
    
    if (tens == 1) and (ones == 8) :
        tens_text = "eighteen"
        ones_text = ""
    
    if (tens == 1) and (ones == 9) :
        tens_text = "nineteen"
        ones_text = ""
    
    if tens == 2:
        tens_text = "twenty"
    
    if tens == 3:
    	tens_text = "thirty"
    
    if tens == 4:
    	tens_text = "forty"
    
    if tens == 5:
    	tens_text = "fifty"
    
    if tens == 6:
    	tens_text = "sixty"
    
    if tens == 7:
    	tens_text = "seventy"
    
    if tens == 8:
    	tens_text = "eighty"
    
    if tens == 9:
    	tens_text = "ninety"
        
    if tens == 0:
        tens_text = ""
    
    if hundred == 1:
    	hundred_text = "one hundred"
    
    if hundred == 2:
    	hundred_text = "two hundred"
    
    if hundred == 3:
    	hundred_text = "three hundred"
    
    if hundred == 4:
    	hundred_text = "four hundred"
    
    if hundred == 5:
    	hundred_text = "five hundred"
    
    if hundred == 6:
    	hundred_text = "six hundred"
    
    if hundred == 7:
    	hundred_text = "seven hundred"
    
    if hundred  == 8:
    	hundred_text = "eight hundred"
    
    if hundred == 9:
    	hundred_text = "nine hundred"
    
    if hundred == 0:
        hundred_text = ""
    
    if thousand == 1:
    	thousand_text = "one thousand"
    
    if thousand == 2:
    	thousand_text = "two thousand"
    
    if thousand == 3:
    	thousand_text = "three thousand"
    
    if thousand == 4:
    	thousand_text = "four thousand"
    
    if thousand == 5:
    	thousand_text = "five thousand"
    
    if thousand == 6:
    	thousand_text = "six thousand"
    
    if thousand == 7:
    	thousand_text = "seven thousand"
    
    if thousand == 8:
    	thousand_text = "eight thousand"
    
    if thousand == 9:
    	thousand_text = "nine thousand"
        
    if thousand == 0:
        thousand_text = ""
    
    if Tthousand == 1:
    	Tthousand_text = "ten"
    
    if Tthousand == 2:
    	Tthousand_text = "twenty" 
    
    if Tthousand == 3:
    	Tthousand_text = "thrirty" 
    
    if Tthousand == 4:
    	Tthousand_text = "forty"
    
    if Tthousand == 5:
    	Tthousand_text = "fifty" 
    
    if Tthousand == 6:
    	Tthousand_text = "sixty" 
    
    if Tthousand == 7:
    	Tthousand_text = "seventy" 
    
    if Tthousand == 8:
    	Tthousand_text = "eighty" 
    
    if Tthousand == 9:
    	Tthousand_text = "ninety" 
    
    if Tthousand == 0:
        Tthousand_text = ""
    
    if Lakh == 1:
    	Lakh_text = "one lakh"
    
    if Lakh == 2:
    	Lakh_text = "two lakh"
    
    if Lakh == 3:
    	Lakh_text = "three lakh"
    
    if Lakh == 4:
    	Lakh_text = "four lakh"
    
    if Lakh == 5:
    	Lakh_text = "five lakh"
    
    if Lakh == 6:
    	Lakh_text = "six lakh"
    
    if Lakh == 7:
    	Lakh_text = "seven lakh"
    
    if Lakh == 8:
    	Lakh_text = "eight lakh"
    	
    if Lakh == 9:
    	Lakh_text = "nine lakh"
    
    if Lakh == 0:
        Lakh_text = ""
    
    if Tlakh == 1:
    	Tlakh_text = "ten"
    
    if Tlakh == 2:
    	Tlakh_text = "twenty"
    
    if Tlakh == 3:
    	Tlakh_text = "thrirty"
    
    if Tlakh == 4:
    	Tlakh_text = "forty"
    
    if Tlakh == 5:
    	Tlakh_text = "fifty"
    
    if Tlakh == 6:
    	Tlakh_text = "sixty"
    
    if Tlakh == 7:
    	Tlakh_text = "seventy"
    
    if Tlakh == 8:
    	Tlakh_text = "eighty" 
    
    if Tlakh == 9:
    	Tlakh_text = "ninety" 
    
    if Tlakh == 0:
        Tlakh_text = ""
    
    if Crore == 1:
    	Crore_text = "one crore"
    
    if Crore == 2:
    	Crore_text = "two crore"
    
    if Crore == 3:
    	Crore_text = "three crore"
        
    if Crore == 4:
   		Crore_text = "four crore"
    
    if Crore == 5:
   		Crore_text = "five crore"
    
    if Crore == 6:
   		Crore_text = "six crore"
    
    if Crore == 7:
   		Crore_text = "seven crore"
    
    if Crore == 8:
    	Crore_text = "eight crore"
    
    if Crore == 9:
    	Crore_text = "nine crore"
    
    if Crore == 0:
        Crore_text = ""
        
     
    ans["text"] = Crore_text + " " + Tlakh_text + " " + Lakh_text + " " + Tthousand_text + " " + thousand_text + " " + hundred_text + " " + tens_text + " " + ones_text
    
Btn = Button(root, text="Get in words", command=convertion)
Btn.place(relx=0.5, rely=0.8, anchor=CENTER)
    
    
root.mainloop()
    
    
