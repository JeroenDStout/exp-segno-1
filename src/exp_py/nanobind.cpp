#include "exp_py/inc_nanobind.h"
#include "exp_py/inc_nanobind_stl.h"

void nb_repo_version(nanobind::module_&);

NB_MODULE(segno_exp_py, m)
{
    nb_repo_version(m);
}
