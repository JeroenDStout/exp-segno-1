// Test test test

#include <iostream>
#include <random>

#include "exp_live/live.h"
#include "repo_version/git_version.h"

int main(int, char*[])
{
    std::cout
      << std::endl
      << "          * * * * * * * ** * * * * * " << std::endl
      << "         * * * Segno Experiment * * * " << std::endl
      << "          * * * * * * * ** * * * * * " << std::endl
      << std::endl
      << gaos::version::get_git_essential_version() << std::endl
      << gaos::version::get_compile_stamp() << std::endl
      << std::endl
      << gaos::version::get_git_history() << std::endl
      << std::endl;

    exp_live::handler_exp_live handler{};
    
    if (handler.prepare() != exp_live::handler_exp_live::handler_result::success)
    { std::cout << "ERROR: Error prepare'ing experiment" << std::endl; return -1; }
    if (handler.init()    != exp_live::handler_exp_live::handler_result::success)
    { std::cout << "ERROR: Error init'ing experiment"    << std::endl; return -1; }
    if (handler.run()     != exp_live::handler_exp_live::handler_result::success)
    { std::cout << "ERROR: Error run'ing experiment"     << std::endl; return -1; }
    if (handler.deinit()  != exp_live::handler_exp_live::handler_result::success)
    { std::cout << "ERROR: Error deinit'ing experiment"  << std::endl; return -1; }
    if (handler.cleanup() != exp_live::handler_exp_live::handler_result::success)
    { std::cout << "ERROR: Error cleanup'ing experiment" << std::endl; return -1; }

    return 0;
}
