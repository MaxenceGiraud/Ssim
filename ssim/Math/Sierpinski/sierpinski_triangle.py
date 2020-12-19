import numpy as np
import matplotlib.pyplot as plt

def sierpinski_triangle(iter = 5,display=True,display_iter = False):

    # Starting points
    tan_angle = np.tan(np.pi/3)
    triangle_list = np.array([[0,0],[3**iter/2,tan_angle*3**iter/2],[3**iter,0],[0,0]]).reshape(1,4,2)

    def draw(triangles):
        for triangle in triangles :
            plt.plot(triangle[:,0],triangle[:,1],c='black')

    for _ in range(iter):

        if display_iter :
            draw(triangle_list)

        new_triangles = []
        for triangle in triangle_list :
            centers = (triangle + np.roll(triangle,-1,axis=0)) /2

            new_triangles.append(np.array([triangle[0],centers[0],centers[2],triangle[0]]))
            new_triangles.append(np.array([centers[0],triangle[1],centers[1],centers[0]]))
            new_triangles.append(np.array([centers[1],triangle[2],centers[2],centers[1]]))
        triangle_list = new_triangles

    
    if display or display_iter: 
        draw(triangle_list)
        plt.axis('equal')
        plt.show()

    return triangle_list

def main():
    s=sierpinski_triangle(6)

if __name__ == "__main__":
    main()