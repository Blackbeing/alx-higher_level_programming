#!/bin/bash
# Send request to 0:5000/catch_me and get 'You got me!' as response
curl -s -X PUT -H 'Origin: School' --url "$(curl -s -X PUT -w '%{redirect_url}' --url 0:5000/catch_me -o /dev/null | xargs curl -s -X PUT -w '%{redirect_url}' -H 'Content-Type: application/x-www-form-urlencoded' -d 'user_id=98' -o /dev/null)"
