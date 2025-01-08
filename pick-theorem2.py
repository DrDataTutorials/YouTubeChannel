# Video de referencia de este script:
# https://www.youtube.com/watch?v=6TiQSJL2zKE


#Subscribe to https://www.youtube.com/@DrDataTutorials
#to be notified about more tutorials like this. 


import matplotlib.pyplot as plt
import math

# Function to calculate area using Pick's Theorem
def pick_theorem(I, B):
    #I: Number of interior points
    #B: Number of boundary points (vertices)
    A = I + B / 2 - 1
    return A

def plot_polygon(vertices):
    # Unzip the vertices for plotting
    x, y = zip(*vertices)
    # Close the polygon by adding the first vertex at the end
    x += (x[0],)
    y += (y[0],)
    # Create the plot
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, marker='o')
    plt.fill(x, y, alpha=0.3)
    plt.title('Lattice Polygon Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    # Calculate the area (assuming a function 'calculate_area' is defined)
    # Replace with actual area calculation logic
    # Display area
    #plt.text(2.5, 4, f'Area: {area:.2f}', fontsize=12, ha='center')
    # Show grid
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    # Show the plot
    plt.xlim(0, 6)
    plt.ylim(0, 5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

#############################################
#Example 1: Triangle
# Define vertices of the lattice polygon
vertices = [(0, 0), (1, 0), (0, 2)]
plot_polygon(vertices)
I = 0  # Number of interior points
B = 4  # Number of boundary points (vertices)
area = pick_theorem(I,B)
print("Total Area:", area)
#############################################

#Example 2: Square
vertices = [(0, 0), (2, 0), (2, 2), (0, 2)]
plot_polygon(vertices)

I = 1  # Number of interior points
B = 8  # Number of boundary points (vertices)
area = pick_theorem(I, B)
print("Total Area:", area)

#############################################

#  Example 3: 
vertices = [(0, 0), (1, 0), (2, 1), (3,2), (4, 3),(5, 4), (4, 5), (3, 4), (2, 3),(1, 2), (0, 1)]
plot_polygon(vertices)

I = 4  # Number of interior points
B = 11  # Number of boundary points (vertices)
# Calculate area
area = pick_theorem(I, B)
print("Total Area:", area)

# Let's test this:

l1 = math.sqrt(4**2 + 4**2)  
l2 = math.sqrt(1**2 + 1**2)  

Area_rectangle = l1 * l2

Area_triangle = 1 * 1 / 2  

Total_area = Area_triangle + Area_rectangle

print("Total Area:", Total_area)

#############################################
