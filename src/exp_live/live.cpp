#include "exp_live/live.h"

#include <iostream>
#include <random>

using namespace exp_live;

auto handler_exp_live::prepare() -> handler_result
{
    return handler_result::success;
}

auto handler_exp_live::init() -> handler_result
{
    return handler_result::success;
}

auto handler_exp_live::run() -> handler_result
{
    return handler_result::success;
}

auto handler_exp_live::deinit() -> handler_result
{
    return handler_result::success;
}

auto handler_exp_live::cleanup() -> handler_result
{
    return handler_result::success;
}