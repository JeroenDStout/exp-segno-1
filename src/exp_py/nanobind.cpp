#include "exp_py/inc_nanobind.h"
#include "exp_py/inc_nanobind_stl.h"

#include "exp_core/my_first_test_decl.h"
#include "exp_core/my_first_test_bind_nano.h"

void nb_repo_version(nanobind::module_&);

NB_MODULE(exp_py, m)
{
    nb_repo_version(m);

    auto sg = m.def_submodule("segno");
    segno::nb_field_row(sg);
}
