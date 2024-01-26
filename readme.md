test
curl --location --request POST 'http://localhost:9000/2015-03-31/functions/function/invocations' \
--header 'X-Hook-Secret: NHAN SET' \
--header 'X-Hook-Signature: 22222' \
--header 'Content-Type: application/json' \
--data-raw '{
"exec_type": "test",
"header": "test_header",
"process_type": "11111",
"project_gid": "xxxxxx",
"events": "1111",
"message": "test"
}'
