#define _USE_MATH_DEFINES
#include<iostream>
#include<cmath>
// #include<matplot/matplot.h>

#include<fstream>

using namespace std;
// using namespace matplot;

void koch_snowflake(bool anti,int iter){

    // Variable definition

    float angle_mov;
    float *xpoints;
    float *ypoints;
    int len_points = 4;
    int len_new_points;
    float xdiff;
    float ydiff;
    float side_eq;
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
    float tan_angle = tan(M_PI/3);
    cout << tan_angle << "\n";
    float xinit[4] = {0.0f, pow(3.0f,(float) iter/2), pow(3.0f,(float) iter), 0.0f};
    xpoints = xinit;
    float yinit[4] = {0.0f, tan_angle * pow(3.0f,(float) iter/2), 0.0f , 0.0f};
    ypoints = yinit;

    cout<< "\nONE : " ;
        
        for (int k = 0; k <= len_points; k++)
        {
            cout << "(" <<xpoints[k] << ", "<< ypoints[k] << "),";
        }
        cout << "\n";


    // TODO draw void function

    for (int i = 0; i < iter; i++)
    {      
        len_new_points = len_points +  (len_points-1)*3;

        float xnew_points[len_new_points];
        float ynew_points[len_new_points];

        xnew_points[0] = xpoints[0];
        ynew_points[0] = ypoints[0];

        for (int j = 0; j < len_points; j++)
        {
            
            // First point of the new triangle
            xdiff = xpoints[j+1] - xpoints[j];
            ydiff = ypoints[j+1] - ypoints[j];

            side_eq = sqrt( pow(xdiff,2) + pow(ydiff,2) )/3;
            angle = atan2(ydiff,xdiff);

            xnew_points[j*4 + 1] = xpoints[j] + xdiff/3;
            ynew_points[j*4 +1] = ypoints[j] + ydiff/3;

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
    
        len_points = len_new_points;

        cout<< "\n\n UPDATE : " ;
        
        for (int k = 0; k <= len_new_points; k++)
        {
            cout << "(" <<xnew_points[k] << ", "<< ynew_points[k] << "),";
        }
        cout << "\n";
         
        
        xpoints = xnew_points;
        ypoints = ynew_points;
    }    
    
}

int main() 
{      
    int depth;
    bool anti;

    cout << "Depth ? "; 
    cin >> depth;

    koch_snowflake(false,depth);  
      
    return 0; 
} 