#!/bin/bash -e

function main {
    source venv/bin/activate
    pytest tests/
    export TEST_RESULT=$?
    deactivate
    exit ${TEST_RESULT}
}

main "$@"
