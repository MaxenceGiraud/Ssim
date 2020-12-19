import numpy as np

def sierpinski_carpet(iter = 5,display=True,display_iter = False):

    # Starting points
    square_list = np.array([[0,0],[3**iter/2,tan_angle*3**iter/2],[3**iter,0],[0,0]]).reshape(1,4,2)

    def draw(squares):
        for square in squares :
            pass
            # TODO

    for _ in range(iter):

        if display_iter :
            draw(square_list)

        new_squares = []
        
        # TODO

    
    if display or display_iter: 
        draw(square_list)
        plt.axis('equal')
        plt.show()

    return square_list

def main():
    s=sierpinski_carpet(6)

if __name__ == "__main__":
    main()