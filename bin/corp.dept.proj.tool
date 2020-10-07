#! /usr/bin/env bash

# bash ------------------------------------------------------------------------

${BASH_DEBUG:+trap '(read -p "[${BASH_SOURCE}:${LINENO}] [${BASH_COMMAND}] ")' DEBUG}


# location --------------------------------------------------------------------

set -eu
readonly _REALPATH=$(realpath "${BASH_SOURCE[ 0 ]}")
readonly _BASENAME=$(basename "${_REALPATH}")
readonly _DIRNAME=$(dirname "${_REALPATH}")
readonly _ROOT=$(dirname "${_DIRNAME}")
readonly _PREFIX=$(dirname "${_ROOT}")


# execute ---------------------------------------------------------------------

exec ${_ROOT}/bin/venv-python -m ${_BASENAME} "${@}"

