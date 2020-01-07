//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// copyright: 2010 to the present, california institute of technology.
// all rights reserved. united states government sponsorship acknowledged.
// any commercial use must be negotiated with the office of technology transfer
// at the california institute of technology.
// 
// this software may be subject to u.s. export control laws. by accepting this
// software, the user agrees to comply with all applicable u.s. export laws and
// regulations. user has the responsibility to obtain export licenses,  or other
// export authority as may be required before exporting such information to
// foreign countries or providing access to foreign persons.
// 
// installation and use of this software is restricted by a license agreement
// between the licensee and the california institute of technology. it is the
// user's responsibility to abide by the terms of the license agreement.
//
// Author: Giangi Sacco
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#include <iostream>
#include <fstream>
#include <complex>
#include <cmath>
using namespace std;
int main(int argc,char ** argv)
{
    double pi = atan2(0,-1);
    if(argv[1][0] == '1')
    {
        ofstream fout1("complexPolarBIP");
        ofstream fout("complexXYBIP");
        int cnt = 0;
        complex<double> arr[24];//12 complex elements 2 bands
        complex<double> arr1[24];//12 complex elements 2 bands
        for(int i = 0; i < 3; ++i)
        {
            for(int j = 0; j < 4; ++j)
            {
                double x = 1.23*(i + 1);
                double y = 4.2*(j + 1);
                arr[cnt] = complex<double>(x,y);
                arr[cnt+1] = complex<double>(2*x,3*y);
                arr1[cnt] = complex<double>(sqrt(x*x + y*y),atan2(y,x));
                arr1[cnt+1] = complex<double>(sqrt(4*x*x + 9*y*y),atan2(3*y,2*x));
                ++cnt;
                ++cnt;
            }
        }
        fout.write((char *) &arr[0],24*sizeof(complex<double>));
        fout1.write((char *) &arr1[0],24*sizeof(complex<double>));
        fout.close();
        fout1.close();
    }
}
