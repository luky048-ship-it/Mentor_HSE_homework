#!/bin/bash
curl -s -X POST "https://api.telegram.org/bot$1/sendMessage" -d chat_id="$2" -d text="$3"