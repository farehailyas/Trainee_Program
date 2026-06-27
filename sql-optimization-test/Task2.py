from db_connection import connect_db
import pandas as pd

def get_connection():
    try:
        conn = connect_db()
        return conn
    except Exception as e:
        print("cannot get connection")


"""This is a correlated subquery which runs subquery for every record in the outer query, orders have 99441 records and payments have 99440 records 
    which means overall operation cost is 99441 * 99440 which is almost 9.8 billion operations. which takes about 22 minutes
 """

def subquery(conn):
    cur = conn.cursor()
    print("running subqury")
    query = """EXPLAIN ANALYZE SELECT o.order_id, o.customer_id, p.payment_value, p.payment_type
            FROM olist_orders_dataset o
            JOIN olist_order_payments_dataset p ON o.order_id = p.order_id
            WHERE p.payment_value > (
                SELECT AVG(p2.payment_value)
                FROM olist_order_payments_dataset p2
                WHERE p2.payment_type = p.payment_type
            )
        """
    # result = pd.read_sql(query , conn)
    # print(result)
    cur.execute(query)
    result = cur.fetchall()      
    print("\n".join([row[0] for row in result]))


"""using cte to separate the logic of calculating average payment per payment type and then joiining with same payment type , 
    which is done in linear time complexity.hence reducing the performance cost and run in 0.09 s.
 """

def create_index(conn):
    cur = conn.cursor()
    query = """CREATE INDEX idx_payment_type ON olist_order_payments_dataset(payment_type)"""
    cur.execute(query)
    conn.commit()
    cur.close()
    print("Index created")


def rewrite_cte(conn):
    cur = conn.cursor()

    query = """EXPLAIN ANALYZE WITH avg_payment AS( SELECT olist_order_payments_dataset.payment_type, AVG(olist_order_payments_dataset.payment_value) as avg_payment_value
                FROM olist_order_payments_dataset
                GROUP BY olist_order_payments_dataset.payment_type 
            ) 
            
            SELECT olist_orders_dataset.order_id, olist_orders_dataset.customer_id, olist_order_payments_dataset.payment_value, olist_order_payments_dataset.payment_type
            FROM olist_orders_dataset 
            LEFT JOIN olist_order_payments_dataset  
            ON olist_orders_dataset.order_id = olist_order_payments_dataset.order_id
            LEFT JOIN avg_payment 
            ON olist_order_payments_dataset.payment_type =  avg_payment.payment_type
            WHERE olist_order_payments_dataset.payment_value > avg_payment.avg_payment_value
    """
    # result = pd.read_sql(query , conn)
    # print(result)
    cur.execute(query)
    result = cur.fetchall()      
    print("\n".join([row[0] for row in result]))

conn = get_connection()
rewrite_cte(conn)
# subquery(conn)
# create_index(conn)