#  *
#  * *
#  * * *
#  * * * *

# rows = int(input("Enter number of rows: "))
# star=1
# for row in range(rows):
#     for col in range(star):
#         print("*",end=" ")
#     print()

# for i in range(1,rows+1):
#     for j in range(i):
#         print("*",end=" ")
#         star+=1
#     print()


#        *
#      * *
#    * * *
#  * * * *

# rows = int(input("Enter number of rows: "))
# spaces = rows-1
# star = 1
# for row in range(rows):
#     for col in range(spaces):
#         print(" ", end=" ")
#     for col in range(star):
#         print("*", end=" ")
#     star += 1
#     spaces -= 1
#     print()

# * * * *
# * * *
# * *
# *

# rows = int(input("Enter number of rows: "))
# for row in range(rows,0,-1):
#     for i in range(row):
#         print("*",end=" ")
#     print()


# * * * *
#   * * *
#     * *
#       *

# rows = int(input("Enter number of rows: "))
# stars = rows
# spaces = 0
# for row in range(rows, 0, -1):
#     for i in range(spaces):
#         print(" ", end=" ")
#     for i in range(stars):
#         print("*",end=" ")
#     spaces += 1
#     stars -= 1
#     print()


#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# star = 1
# rows = int(input("Enter number of rows: "))
# spaces = rows - 1
# for i in range(rows):
#     for j in range(spaces):
#         print(" ", end=" ")
#     for k in range(star):
#         print("*", end=" ")
#     star+=2
#     spaces-=1
#     print()


# * * * * *
#   * * *
#     *

# rows = int(input("Enter number of rows: "))
# star = rows+4
# spaces = 0
# for i in range(rows, 0, -1):
#     for j in range(spaces):
#         print(" ", end=" ")
#     for k in range(star):
#         print("*", end=" ")
#     star-=2
#     spaces+=1
#     print()

# *
# * *
# * * *
# * *
# *

# rows = int(input("Enter number of rows: "))
# star = 1
# for i in range(rows):
#     for  j in range(star):
#         print("*",end=" ")
#     if i < rows // 2:
#         star = star + 1
#     else:
#         star = star - 1
#     print()

# * *
# * *
# * * * *
# * * * *
# * * * * * *
# * * * * * *

# star=2
# rows=int(input("Enter the number of rows: "))
# for row in range(rows):
#     for column in range(star):
#         print("*",end=" ")
#     if row%2!=0:
#         star+=2
#     print()

#      *
#    * * *
#  * * * * *
#    * * *
#      *

# rows=int(input("Enter the number of rows: "))
# star = 1
# spaces = rows // 2 + 1
# for row in range(rows):
#     for col in range(spaces):
#         print(" ",end=" ")
#     for i in range(star):
#         print("*",end=" ")
#     if row < rows//2:
#         spaces -= 1
#         star +=2
#     else:
#         spaces += 1
#         star -=2
#     print()

# * * * *
# *     *
# *     *
# * * * *

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# for row in range(rows):
#     for column in range(columns):
#         if row == rows-1 or column == columns-1 or row == 0 or column == 0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#     *
#     *
# * * * * *
#     *
#     *

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# for row in range(rows):
#     for column in range(columns):
#         if row == rows//2 or column == columns//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# #
# * *
# # # #
# * * * *
# # # # # #


# rows = int(input("Enter the number of rows: "))
# symbol = 1
# for row in range(rows):
#     for column in range(symbol):
#         if row % 2 == 0:
#             print("#", end=" ")
#         else:
#             print("*", end=" ")
#     symbol += 1
#     print()

# 1 0 1 0
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# for row in range(rows):
#     for column in range(columns):
#         if row % 2 == 0:
#             if column % 2 == 0:
#                 print("1", end=" ")
#             else:
#                 print("0", end=" ")
#         else:
#             if column % 2 != 0:
#                 print("1", end=" ")
#             else:
#                 print("0", end=" ")
#     print()

#       *
#     * *
#   * * *
# * * * *
# * * *
# * *
# *

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# spaces = columns - 1
# star=1
# for row in range(rows):
#     for column in range(spaces):
#         print(" ", end=" ")
#     for col in range(star):
#         print("*", end=" ")
#     if row < rows//2:
#         star = star + 1
#         spaces = spaces - 1
#     else:
#         star = star - 1
#     print()

# A
# AB
# ABC
# ABCD

# character = 1
# rows = int(input("Enter the number of rows: "))
# for i in range(rows):
#     value = 65
#     for j in range(character):
#         print(chr(value), end="")
#         value += 1
#     character += 1
#     print()

# 9
# 8 7
# 6 5 4
# 3 2 1 0

# value=9
# count=1
# rows = int(input("Enter the number of rows: "))
# for i in range(rows):
#     for j in range(count):
#         print(value,end=" ")
#         value=value-1
#     count=count+1
#     print()

#     1
#     2
# 1 2 3 4 5
#     4
#     5

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# for row in range(rows):
#     for column in range(rows):
#         if row == rows//2:
#             print(column+1, end=" ")
#         elif column == columns//2 :
#             print(row+1,end=" ")
#         else:
#             print(" ",end=" ")
#     print()



