import math

# Function to calculate the volume of a sphere
# Formula: Volume = (4/3) * π * r^3
def volume(rad, hgt=None):  # 'hgt' is unused, just added to match Flask route input
    return (4/3) * math.pi * rad**3

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius : "))
    vol = volume(radius)
    print("\nThe Volume of a Sphere = ", vol)

if __name__ == '__main__':
    prompt()
