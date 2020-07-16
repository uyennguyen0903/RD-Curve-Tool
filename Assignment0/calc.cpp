// calculate bitrate (= bit/pixel)

#include <iostream>
#include <fstream>
#include <cassert>
#include <iomanip>      
using namespace std;

main()
{

    //Image' dimensions
    long double width, height, s;
    cout << "Enter width of image :" << endl;
    cin >> width;
    cout << "Enter height of image :" << endl;
    cin >> height;
    s = width * height;

    ifstream read_file("data.txt");
    assert(read_file.is_open());

    ofstream write_output("data.dat");
    assert(write_output.is_open());

    for(int i = 0; i <= 100; i++)
    {
        long double t1, t2;
        read_file >> t1 >> t2;
        write_output << t1/s << " " << t2 << setprecision(9) << endl;
    }

    write_output.close();
    read_file.close();
    
    return 0;
}