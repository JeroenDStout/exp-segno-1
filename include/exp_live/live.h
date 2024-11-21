#pragma once

namespace exp_live {

    struct handler_exp_live {
        enum class handler_result { success, failure };
        
        handler_result prepare();
        handler_result init();
        handler_result run();
        handler_result deinit();
        handler_result cleanup();
    };

}