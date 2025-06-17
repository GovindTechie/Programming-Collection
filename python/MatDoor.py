# n,m = map(int, input().split("Enter width and length(3 time's of width) "))
# # first half
# for i in range(0, n//2) :
#     for j in range(0, ((n//2)-i)*3):
#         print('-', end='')
#     for k in range(0, (i*2+1)):
#         print(".|.", end='')
#     for j in range(0, ((n//2)-i)*3):
#         print('-', end='')
#     print()

# # center line
# for i in range(0, (m-7)//2):
#     print('-', end='')
# print('WELCOME', end='')
# for i in range(0, (m-7)//2):
#     print('-', end='')
# print()

# # second half
# for i in range(n//2-1, -1, -1) :
#     for j in range(0, ((n//2)-i)*3):
#         print('-', end='')
#     for k in range(0, (i*2+1)):
#         print(".|.", end='')
#     for j in range(0, ((n//2)-i)*3):
#         print('-', end='')
#     print()


# simple version
N, M = map(int, input().split(" "))
for i in range(1, N):
    if i % 2 != 0:
        print((".|." * i).center(M, "-"))
print("WELCOME".center(M, "-"))
for i in range(1, N):
    if i % 2 != 0:
        print((".|." * (N - 1 - i)).center(M, "-"))
