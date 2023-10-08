import psycopg2
import os


class Database:
    def __init__(self):
        # Get database configuration from environment variables
        self.dbname = os.environ.get("dbname")
        self.user = os.environ.get("user")
        self.password = os.environ.get("password")
        self.host = os.environ.get("host")
        self.port = os.environ.get("port")

    def __enter__(self):
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type):
        try:
            if exc_type is not None:
                self.connection.rollback()  # Rollback the transaction if an exception occurred
            else:
                self.connection.commit()  # Commit the transaction if no exception occurred
        finally:
            self.cursor.close()
            self.connection.close()























# import psycopg2, os
# from psycopg2 import sql



# # ++++++++++++++++++++++++++++++THIS IS A TEST SCENARIO!++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class Database:
#     def __init__(self, dbname, user, password, host, port):
#         self.connection = psycopg2.connect(
#             dbname=dbname,
#             user=user,
#             password=password,
#             host=host,
#             port=port
#         )
#         self.cursor = self.connection.cursor()

#     def execute_query(self, query, params=None):
#         try:
#             if params:
                # self.cursor.execute(query, params)
#             else:
#                 self.cursor.execute(query)
#             self.connection.commit()
#         except Exception as error:
#             self.connection.rollback()
#             print("Error executing query:", error)

#     def fetch_data(self, query, params=None):
#         try:
#             if params:
#                 self.cursor.execute(query, params)
#             else:
#                 self.cursor.execute(query)
#             return self.cursor.fetchall()
#         except Exception as error:
#             print("Error fetching data:", error)

#     def close_connection(self):
#         self.cursor.close()
#         self.connection.close()

# # Example usage:
# if __name__ == "__main__":
#     # Database configuration
#     host = os.environ.get("host")
#     dbname = os.environ.get("dbname")
#     user = os.environ.get("user")
#     port = os.environ.get("port")
#     password =  os.environ.get("password")

#     # Create a Database instance
#     db = Database(dbname, user, password, host, port)

#     # Example queries
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS users (
#         id SERIAL PRIMARY KEY,
#         username VARCHAR(255),
#         email VARCHAR(255)
#     )
#     """

#     insert_data_query = """
#     INSERT INTO users (username, email) VALUES (%s, %s)
#     """

#     select_data_query = "SELECT * FROM public.shop"

#     # Execute queries
#     # db.execute_query(create_table_query)
#     # db.execute_query(insert_data_query, ("john_doe", "john@example.com"))
#     # db.execute_query(insert_data_query, ("jane_smith", "jane@example.com"))

#     # Fetch and print data
#     shop = db.fetch_data(select_data_query)
#     print("shop:")
#     print(shop)
#     for user in shop:
#         print(user)

#     # Close the database connection
#     db.close_connection()