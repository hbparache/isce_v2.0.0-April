//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// copyright: 2014 to the present, california institute of technology.
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
// Author: Piyush Agram
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





#ifndef WATERMASK_H
#define WATERMASK_H

#ifndef ERR_MESSAGE
#define ERR_MESSAGE cout << "Error in file " << __FILE__ << " at line " << __LINE__  << " Exiting" <<  endl; exit(1);
#endif


class Polygon
{
    private:
        int npoints;
        double **xy;
    public:
        Polygon();
        ~Polygon();
        void allocate(int n);
        void setPoint(int i, double x, double y);
        int isInside(double testx, double testy);
        void print();
};


class WaterBody
{
    private:
        Polygon *shapes;
        int nshapes;
        double x0, y0;
        double dx, dy;
        int width, height;

    public:
        WaterBody(int n);
        ~WaterBody();
        int isWater(double x, double y);
        void allocate(int ind, int n);
        void setShapeData(int ind, int i, double x, double y);
        void setDimensions(int ww, int ll);
        void setTopLeft(double xx, double yy);
        void setSpacing(double ddx, double ddy);
        void fillGrid(char* filename);
        void makemask(char* lonfile, char* latfile, char* outfile);
        void printShape(int i);
};

#endif //WATERMASK_H
