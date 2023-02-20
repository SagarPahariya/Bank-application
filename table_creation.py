
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime

# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = 'passw0rd'
host = 'localhost'
port = 3306
database = 'fna_analytics_test'


# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    print('connecting to the server...')

    # “dialect+driver://username:password@host:port/database”.
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )


class CreateTable:

    def userrole_tblcrtn(self, meta):
        Table("user_role", meta,
              Column("role_id", Integer, primary_key=True),
              Column("role_name", String(500), nullable=False),
              Column("created_date", DateTime, nullable=False),
              Column("last_updated_date", DateTime, nullable=False),
              )

    def accounttype_tblcrtn(self, meta):
        Table("account_type", meta,
              Column("account_id", Integer, primary_key=True),
              Column("account_type", String(500), nullable=False),
              Column("created_date", DateTime, nullable=False),
              Column("last_updated_date", DateTime, nullable=False),
              )

    def legalentity_tblcrtn(self, meta):
        Table("legal_entity", meta,
              Column("legalentity_id", Integer, primary_key=True),
              Column("legalentity_name", String(500), nullable=False),
              Column("created_date", DateTime, nullable=False),
              Column("last_updated_date", DateTime, nullable=False),
              )

    def taskreason_tblcrtn(self, meta):
        Table("task_reason", meta,
              Column("reason_id", Integer, primary_key=True),
              Column("taskreason", String(500), nullable=False),
              Column("created_date", DateTime, nullable=False),
              Column("last_updated_date", DateTime, nullable=False),
              )



if __name__ == '__main__':
    print('program start for Table Creation...')

    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection()
        print(f"Connection to the '{host}' for user '{user}' created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

    # try:
    meta = MetaData()
    # print('Meta object created...', meta.info)

    table_creation = CreateTable()
    table_creation.userrole_tblcrtn(meta)




    meta.create_all(engine)

    print('Table successfully created')


    # except Exception as ex:
    #     print("Issue while creating table : \n", ex)

    print('END...')
