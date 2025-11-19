#!/bin/bash
find . -name "*.log" -type f -printf "%T@ %p\n" | sort -n | head -5 | cut -d' ' -f2-