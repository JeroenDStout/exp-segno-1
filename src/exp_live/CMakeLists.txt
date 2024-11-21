init_directory(exp_live)

# Define the exp_live project
init_project(exp_live "experiment")

# Sources
setup_project_source(exp_live "core"
  src:
    main.cpp
    live.cpp
  include:
    live.h
)

# Target
configure_project_executable(exp_live)
configure_project_console(exp_live)
configure_cxx_target(exp_live)
configure_target_outputs(exp_live)
configure_publish_exec(exp_live)
	
add_dependencies(exp_live exp_core repo_version)
target_link_libraries(exp_live PRIVATE exp_core)
