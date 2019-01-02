from datetime import date 
import holidays 
acet_holidays = holidays.Acet() 
  

for ptr in holidays.Acet(years=2019).items(): 
    print(ptr) 
