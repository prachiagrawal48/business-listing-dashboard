import mysql.connector

print("Starting")

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        auth_plugin="mysql_native_password",
        use_pure=True,
        connection_timeout=5
    )

    print("Connected!")

except Exception as e:
    print("ERROR:", repr(e))