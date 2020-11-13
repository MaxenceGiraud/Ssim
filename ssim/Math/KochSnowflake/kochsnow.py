import numpy as np
import matplotlib.pyplot as plt

def koch_snowflake(iterations=2,display_iter=False,display=True):
    # Starting points
    tan_angle = np.tan(np.pi/3)
    points = [[0,0],[3**iterations/2,tan_angle*3**iterations/2],[3**iterations,0],[0,0]]

    def draw(points):
        points_np = np.array(points)
        plt.figure(figsize=(10,10))
 
        plt.plot(points_np[:,0],points_np[:,1])
        plt.axis('square')

    for _ in range(iterations-1):
        new_points = [] 
        for i in range(len(points)-1) : 
            new_points.append(points[i]) # Add old point to new list

            x_diff = points[i+1][0]-points[i][0]
            y_diff = points[i+1][1]-points[i][1]

            side_eq = np.sqrt( (x_diff)**2 + (y_diff)**2 )/3  # Signed len of new triangle side (/3)
            angle = np.arctan2(y_diff,x_diff) # angle between 2 points
            
            # First point of new triangle (first third of line)
            new_x = points[i][0] + x_diff/3
            new_y = points[i][1] + y_diff/3
            new_points.append([new_x,new_y])

            # Top of new triangle
            new_x += side_eq * np.cos(angle+np.pi/3)
            new_y += side_eq * np.sin(angle+np.pi/3)
            new_points.append([new_x,new_y])

            # Third and last point of new triangle (first third of line)
            new_x = points[i][0] + 2*x_diff/3
            new_y = points[i][1] + 2*y_diff/3
            new_points.append([new_x,new_y])
            
        new_points.append(points[-1]) # Add last point
        points = new_points

        if display_iter : 
            draw(points)

    if display and not display_iter:
        draw(points)

    return points