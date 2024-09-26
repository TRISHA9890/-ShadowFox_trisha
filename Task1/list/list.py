#calculate the number of members in the Justice league
justice_league=["superman","batman","wonder women","flash","aquman","green latern"]
number_of_members=len(justice_league)#to calculate the members
print(number_of_members)


#batman recurited batgirl& nightwig as new members.add them to your list
#append:add items
justice_league.append("batgirl")
justice_league.append("nightwig")
print(justice_league)


#wonder women is now the leader of the justice league.move her to beginning of the list
justice_league.remove("wonder women")
justice_league.insert(0,"wonder women")#wonder women in beginning of the list
print(justice_league)


#separate aquman and flash
justice_league.remove("green latern")
index_aquman=justice_league.index("aquman")
justice_league.insert(index_aquman + 1,"green latern")
print("updated justice league:",justice_league)

#superman decide to assemble a new team
justice_league=["cyborg","shazam","hawkgirl","martin manhunter","green arrow"]
print("new justice league:",justice_league)

#sort the justice league
justice_league.sort()
print("sort the justice league:",justice_league)
#the new leader will be:cyborg
