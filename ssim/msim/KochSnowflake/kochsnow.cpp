#define _USE_MATH_DEFINES
#include<iostream>
#include<cmath>
// #include<matplot/matplot.h>
#include<fstream>

using namespace std;
// using namespace matplot;

void koch_snowflake(bool anti,int iter){

    // Variable definition

    float angle_mov; // angle of triangle
    double *xpoints; // x coordonates of points
    double *ypoints; // y coordonates of points
    int len_points = 4; // number of points
    int len_new_points; // number of points in next step
    float xdiff; // x difference between point and next point
    float ydiff; // y difference between point and next point
    float side_eq; // length of triangle's side
    float angle;


    if (anti == false)
    {
        angle_mov = - M_PI /3;
    }
    else
    {
        angle_mov = M_PI /3;
    }

    // define first points
    const double tan_angle = tan(M_PI/3);
    double xinit[4] = {0, pow(3,iter+2)/2, pow(3,(iter+2)), 0};
    xpoints = xinit;
    double yinit[4] = {0, tan_angle * pow(3,(iter+2))/2, 0 , 0};
    ypoints = yinit;

    cout<< "\nONE : " ;
        
        for (int k = 0; k < len_points; k++)
        {
            cout << "(" <<xpoints[k] << ", "<< ypoints[k] << "),";
        }
        cout << "\n";


    // TODO draw void function

    for (int i = 0; i < iter; i++)
    {      
        len_new_points = len_points +  (len_points-1)*3;
        cout << "\nLen new points  = " << len_new_points << "\n";

        double xnew_points[len_new_points];
        double ynew_points[len_new_points];

        // First point
        xnew_points[0] = xpoints[0];
        ynew_points[0] = ypoints[0];

        for (int j = 0; j < len_points; j++)
        {
            
            // First point of the new triangle
            xdiff = xpoints[j+1] - xpoints[j];
            ydiff = ypoints[j+1] - ypoints[j];

            side_eq = sqrt( pow(xdiff,2) + pow(ydiff,2) )/3;
            angle = atan2(ydiff,xdiff);
            // cout << ydiff ;

            xnew_points[j*4 + 1] = xpoints[j] + xdiff/3;
            ynew_points[j*4 + 1] = ypoints[j] + ydiff/3;

            // Top of the triangle
            xnew_points[j*4+2] = xnew_points[j*4 + 1] + side_eq * cos(angle+angle_mov);
            ynew_points[j*4+2] = ynew_points[j*4 + 1] + side_eq * sin(angle+angle_mov);

            // Third point of the triangle
            xnew_points[j*4+3] = xpoints[j] + 2 * xdiff/3;
            ynew_points[j*4+3] = ypoints[j] + 2 * ydiff/3;

            // Old point
            xnew_points[j*4 +4] = xpoints[j];
            ynew_points[j*4 +4] = ypoints[j];

        }

        xnew_points[len_new_points] = xpoints[len_points];
        ynew_points[len_new_points] = ypoints[len_points];

        len_points = len_new_points;

        cout<< "\n\n UPDATE : " ;
        
        for (int k = 0; k < len_new_points; k++)
        {
            cout << "k="<<k <<" (" <<xnew_points[k] << ", "<< ynew_points[k] << "),";
        }
        cout << "\n";


        double tmpx[len_new_points];
        double tmpy[len_new_points];

        std::copy(xnew_points,&xnew_points[len_new_points],tmpx);
        std::copy(ynew_points,&ynew_points[len_new_points],tmpy);

        xpoints = tmpx;
        ypoints = tmpy;
    }    

    cout<< "\n\n END : " ;
        
        for (int k = 0; k < len_points; k++)
        {
            cout << "(" <<xpoints[k] << ", "<< ypoints[k] << "),";
        }
        cout << "\n";
    
}

int main() 
{      
    int depth = 1;
    bool anti;

    // cout << "Depth ? "; 
    // cin >> depth;

    koch_snowflake(false,depth);  
      
    return 0; 
} 