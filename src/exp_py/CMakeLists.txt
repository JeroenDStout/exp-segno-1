init_directory(exp_py)

# Define the tod_py project
init_project(exp_py "experiment")

# Sources
setup_project_source(exp_py "nanobind"
  src:
    nanobind.cpp
    nanobind_meta.cpp
)
setup_project_source(exp_py "third_party"
  include:
    inc_nanobind.h
    inc_nanobind_stl.h
)

# Target
configure_project_nanobind(exp_py)
configure_cxx_target(exp_py)
configure_target_outputs(exp_py)
configure_project_eigen(exp_py)
	
add_dependencies(exp_py exp_core repo_version)
target_link_libraries(exp_py PRIVATE exp_core)
