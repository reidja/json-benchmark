#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"
#include <iostream>
#include "rapidjson/filereadstream.h"
#include "rapidjson/filewritestream.h"
#include <cstdio>
#include <ctime>

using namespace rapidjson;

int main(int argc, char** argv) {
    // handle command line arguments
    if(argc != 3) {
        std::cout << "Usage: ./test_cpp <input> <output>" << std::endl;
        return 1;
    }

    // read and parse input
	std::clock_t read_start = std::clock();
    char readBuffer[65536];
    FILE* input_file = fopen(argv[1], "rb");
    FileReadStream is(input_file, readBuffer, sizeof(readBuffer));
    Document d;
    std::clock_t parse_start = std::clock();
    d.ParseStream(is);
    std::clock_t parse_end = std::clock();
    fclose(input_file);
    std::clock_t read_end = std::clock();

    // serialize and write output
    std::clock_t write_start = std::clock();
    FILE* output_file = fopen(argv[2], "wb");
	char writeBuffer[65536];
	FileWriteStream os(output_file, writeBuffer, sizeof(writeBuffer));
    std::clock_t serialize_start = std::clock();
	Writer<FileWriteStream> writer(os);
	d.Accept(writer);
    std::clock_t serialize_end = std::clock();
	fclose(output_file);
	std::clock_t write_end = std::clock();

    // stats
	std::cout << "r:" << (read_end - read_start) / (double) (CLOCKS_PER_SEC) << std::endl;
    std::cout << "p:" << (parse_end - parse_start) / (double) (CLOCKS_PER_SEC) << std::endl;
	std::cout << "w:" << (write_end - write_start) / (double) (CLOCKS_PER_SEC ) << std::endl;
    std::cout << "s:" << (serialize_end - serialize_start) / (double) (CLOCKS_PER_SEC) << std::endl;
    return 0;
}