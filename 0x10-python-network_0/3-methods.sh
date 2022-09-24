#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -sIL "$1" -X OPTIONS | grep -i Allow | cut -d " " -f2-
