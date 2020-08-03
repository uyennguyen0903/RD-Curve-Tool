// calculate bitrate (= bit/pixel)

#include <cassert>
#include <fstream>
#include <iomanip>
#include <iostream>
using namespace std;

main(int argc, char* argv[]) {
  if (argc == 1) {
    std::cout << "./calc input_filename output_filename img_num img_width "
                 "img_height\n";
    return 0;
  }
  std::ifstream input(argv[1]);
  std::ofstream output(argv[2]);
  std::string string_pic_num = argv[3];
  std::string string_pic_width = argv[4];
  std::string string_pic_height = argv[5];

  int pic_num = 0;
  for (auto t : string_pic_num) pic_num = pic_num * 10 + (t - '0');
  pic_num++;

  int pic_width = 0;
  for (auto t : string_pic_width) pic_width = pic_width * 10 + (t - '0');

  int pic_height = 0;
  for (auto t : string_pic_height) pic_height = pic_height * 10 + (t - '0');

  long double s = (1.0 * pic_width) * (1.0 * pic_height);

  for (int i = 1; i <= 101 * pic_num; i++) {
    long double t1, t2;
    input >> t1 >> t2;
    output << t1 / s << " " << t2 << setprecision(9) << endl;
  }

  return 0;
}