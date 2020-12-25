import numpy as np
import math as m

# asking for number of links
i = int(input("enter the number of link\n"))
print("now enter the DH parameters for each link (a, \u03B1, d, \u03F4)")
no_of_link = np.arange(i)
print(no_of_link)

# Resizing the array into link*4 matrix
dh = np.array([])
dh.resize((i, 4))

# Enter the value of "a"
print("enter the value of a")
for i in range(len(no_of_link)):
    a = float(input())
    dh[i][0] = a
    #print("\n", dh)


# Enter the value of "α"
print("enter the value of α")
for i in range(len(no_of_link)):
    angle_alpha_input = float(input())
    angle_alpha = angle_alpha_input
    dh[i][1] = angle_alpha
    #print("\n", dh)

# Enter the value of "d"
print("enter the value of d")
for i in range(len(no_of_link)):
    linklen_d = float(input())
    dh[i][2] = linklen_d
    #print("\n", dh)

# Enter the value of "ϴ"
print("enter the value of ϴ")
for i in range(len(no_of_link)):
    angle_theta_input = float(input())
    angle_theta = angle_theta_input
    dh[i][3] = angle_theta
    #print("\n", dh)

print(dh)

# Transformation Matrix Function
def Trans_Mat():
    T_i = np.round_(np.array([(np.cos(np.deg2rad(dh[i][3])), -np.sin(np.deg2rad(dh[i][3]))*np.cos(np.deg2rad(dh[i][1])), np.sin(np.deg2rad(dh[i][3]))*np.sin(np.deg2rad(dh[i][1])), dh[i][0]*np.cos(np.deg2rad(dh[i][3]))),
    (np.sin(np.deg2rad(dh[i][3])), np.cos(np.deg2rad(dh[i][3]))*np.cos(np.deg2rad(dh[i][1])), -np.cos(np.deg2rad(dh[i][3]))*np.sin(np.deg2rad(dh[i][1])), dh[i][0]*np.sin(np.deg2rad(dh[i][3]))),
    (0,np.sin(np.deg2rad(dh[i][1])),np.cos(np.deg2rad(dh[i][1])),dh[i][2]),
    (0,0,0,1)]),decimals = 3)
    return T_i

Homo_Mat = np.eye(4)
print("\nThis is default Homogeneous Transformation \n", Homo_Mat)
print("\nThis is transformation matrix \n")

for i in range(len(no_of_link)):
    print("\nlink no.: ", i+1, "\n")
    print(Trans_Mat())
    
    Homo_Mat = np.dot(Homo_Mat,Trans_Mat())
    
print("\n This is final HT Matrix\n",Homo_Mat)