init_directory(segno)

# Define the Version project
init_project(segno "support")

# Sources static
setup_project_source(segno "lang"
  src:
    segno_grammar.g4
)
setup_project_source(segno "processor/core"
  script:
    segno_proc.py
    segno/sg_listener.py
    segno/sg_listener_debug.py
)
setup_project_source(segno "processor/objects"
  script:
    segno/sg_translation_unit.py
    segno/sg_field.py
    segno/sg_operator.py
    segno/sg_pass.py
    segno/sg_identifier.py
    segno/sg_typename.py
)
setup_project_source(segno "processor/generator"
  script:
    segno/writer_ctx.py
    segno/generator_base.py
    segno/generator_cxx_cpp.py
    segno/generator_cxx_decl.py
    segno/generator_cxx_impl.py
    segno/generator_cxx_bind_nano.py
)

# Antlr files
set(antlr_generated_files)
antlr_py_build_single(${abs_can_src}/segno_grammar.g4 "antlr" antlr_generated_files)
setup_project_source_specific(segno "lang/generated" "generated;script" ${antlr_generated_files})
 
# Target
configure_project_script(segno)