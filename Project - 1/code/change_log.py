import pandas as pd

change_log = pd.DataFrame({
    "Change_ID":["CR01","CR02","CR03","CR04"],
    "Description":["Filled missing CouponCode values as N/A ","Searched for duplicate rows","Standardized text format","Rounded price values"],
    "Impact":["preserved 319 records","No duplicated records found","Improved consistency","Improved consistency"],
    "Status":["Resolved","Resolved","Resolved","Resolved"]
})

change_log.to_excel("C:\\Users\\Mahi\\OneDrive\\Desktop\\Change_log.xlsx",index=False)

print("Change_log.xlsx created successfully")