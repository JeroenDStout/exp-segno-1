init_directory(exp_core)

# Define the tod_core project
init_project(exp_core "experiment")

# Sources
setup_project_source(exp_core "core"
  src:
    core.cpp
    my_first_test.segno
  include:
    operators_impl.h
)
setup_project_source(tod_core "third_party"
  include:
    inc_eigen.h
)

# Segno
set(segno_generated_cpp)
set(segno_generated_h)
segno_proc_single_cxx(${abs_can_src}/my_first_test.segno "" "" segno_generated_cpp segno_generated_h)
setup_project_source_specific(exp_core "core/generated" "generated;src"     ${segno_generated_cpp})
setup_project_source_specific(exp_core "core/generated" "generated;include" ${segno_generated_h})

# Target
configure_project_static_lib(exp_core)
configure_project_segno(exp_core)
configure_cxx_target(exp_core)
configure_target_outputs(exp_core)
configure_publish_exec(exp_core)