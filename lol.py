# import re

# # ------------- Was a Match Found ----------

# # Search for ape in the string

# if re.search("ape", "The ape was at the apex"):
#     print("There is an age")





# finditer returns an itaretor of matching objects
# You can use span to get the location


# import re
# theStr = "The ape was at the apex"
# print(theStr)
# for i in re.finditer("ape",theStr):
#     # Span returns a tuple
#     locTuple = i.span()

#     print(locTuple)

#     # Slice the match out using the tuple values
#     print(theStr[locTuple[0]:locTuple[1]])







import re

# -------- Matching WhiteSpace ---------

# \s is the same as [\f\n\r\t\v]
# \s is the same as [^\f\n\r\t\v]

# Check for valid first and last name with a space

if re.search("\w{2,20}\s\w{2,20}","Toshio Muramatsu"):
    print("It is a valid full name")