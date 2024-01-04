Database runs in the namespace of the container. So the Database URL must contain the container name instead of localhost.

Hashed contents in Linux
echo -n "content" | base64

Hashed contents in Windows
powershell "[convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes(\"postgresql://postgres:admin@localhost:5432/db\"))"
