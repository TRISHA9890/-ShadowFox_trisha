"""expenses"""
your_expenses={
    "Hotel":1200,
    "Food":800,
    "Transportation":500,
    "Attraction":300,
    "Miscellaneous":200

}

partner_expenses={
    "Hotel":1000,
    "Food":900,
    "Transportation":600,
    "Attraction":400,
    "Miscellaneous":200
}
your_total_expenses = sum(your_expenses.values())
print("Your total expenses: ", your_total_expenses)

partner_total_expenses = sum(partner_expenses.values())
print("Your partner's total expenses: ", partner_total_expenses)



if your_total_expenses > partner_total_expenses:
    print("You spent more money overall:")
elif your_total_expenses< partner_total_expenses:
    print("Your partner spent more money overall.")
else:
    print("You and your partner spent the same amount.")

max_diff=0
max_diff_category = ""
for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        max_diff_category = category
print("The category with the most significant difference in spending is: ", max_diff_category)
print("The difference is: ", max_diff)