#!/bin/sh
SCRIPT_DIR=$(dirname $(dirname $(readlink -f "$0")))

find $SCRIPT_DIR -name "*.pyc" -exec svn revert {} \;
find $SCRIPT_DIR -name "*.pyc" -exec svn delete {} \;
svn -R ps svn:ignore -F $SCRIPT_DIR/script/pyc_ig $SCRIPT_DIR