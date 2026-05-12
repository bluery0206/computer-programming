# YOU CANNOT RUN THIS UNTIL YOU DOWNLOAD THE
# LIBRARY USED WHICH IS MATPLOTLIB

from matplotlib import pyplot as plt

# Android
# you have to install matplotlib in your pydroid

# PC
# open terminal or cmd, then type
#       python3 -m pip install matplotlib
# then after installation, suwayi ug 
# pa run ug balik ang program

profile = {
    "username": "myusername",
    "password": "mypassword",
    "profile": [
        [254,254,254,254,254,254,254,254,254,254,254,254,254,254,254],
        [254,254,254,254,254,  0,  0,  0,  0,  0,254,254,254,254,254],
        [254,254,254,  0,  0,200,200,200,200,200,  0,  0,254,254,254],
        [254,254,  0,200,200,200,200,200,200,200,200,200,  0,254,254],
        [254,254,  0,200,200,  0,200,200,200,  0,200,200,  0,254,254],
        [254,  0,200,200,200,  0,200,200,200,  0,200,200,200,  0,254],
        [254,  0,200,200,200,  0,200,200,200,  0,200,200,200,  0,254],
        [254,  0,200,200,200,200,200,200,200,200,200,200,200,  0,254],
        [254,  0,200,200,200,200,200,200,200,200,200,200,200,  0,254],
        [254,  0,200,200,  0,200,200,200,200,200,  0,200,200,  0,254],
        [254,254,  0,200,200,  0,200,200,200,  0,200,200,  0,254,254],
        [254,254,  0,200,200,200,  0,  0,  0,200,200,200,  0,254,254],
        [254,254,254,  0,  0,200,200,200,200,200,  0,  0,254,254,254],
        [254,254,254,254,254,  0,  0,  0,  0,  0,254,254,254,254,254],
        [254,254,254,254,254,254,254,254,254,254,254,254,254,254,254],
    ]
}

print(profile['username'])
print(profile['password'])

# this ones complex stuff but this just shows the list as an image
plt.figure(figsize=(4,4))
plt.imshow(profile['profile'],cmap='gray')
plt.show()
