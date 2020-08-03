#include <fstream>
#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
  if (argc == 1) {
    std::cout << "./gen_data output_file img_num original_img_format\n";
    return 0;
  }
  std::ofstream output(argv[1]);
  std::string string_pic_num = argv[2];
  std::string img_format = argv[3];
  // std::string quality = argv[4];
  // output << quality << "\n";
  int pic_num = 0;
  for (auto t : string_pic_num) pic_num = pic_num * 10 + (t - '0');

  std::string s = "dump_";

  for (int i = 0; i <= pic_num; i++) {
    //    output << dir << "/";
    output << s;
    if (i < 10) {
      output << "000";
    } else if (i < 100) {
      output << "00";
    } else if (i < 1000) {
      output << "0";
    }
    output << i << "." << img_format << " -o ";

    output << s;
    if (i < 10) {
      output << "000";
    } else if (i < 100) {
      output << "00";
    } else if (i < 1000) {
      output << "0";
    }
    output << i << ".webp"
           << "\n";
  }

  return 0;
}
