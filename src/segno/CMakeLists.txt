init_directory(segno)

# Define the Version project
init_project(segno "support")

# Sources static
setup_project_source(segno "lang"
  src:
    segno_grammar.g4
)
setup_project_source(segno "processor"
  script:
    segno_proc.py
)

# Antlr files
set(antlr_generated_files)
antlr_py_build_single(${abs_can_src}/segno_grammar.g4 "antlr" antlr_generated_files)
setup_project_source_specific(segno "lang/generated" "generated;script" ${antlr_generated_files})
 
# Target
configure_project_script(segno)