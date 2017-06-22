import logging
import psycopg2
import mock
from ddt import ddt, data, unpack
import unittest

query = ("SELECT COUNT (anatomic_site_name) FROM public.dw_study_anatomic_site WHERE anatomic_site_name = '{}'"
            .format('Leukemia'))


def get_result_from_ctrp(query):
    """
    SQL Query the CTRP database for specified result
    :param query:
    :return: list result of query
    """

    cursor = get_AWS_CTRP_connection()

    try:
        cursor.execute(query)
    except:
        logging.info("I can't SELECT from bar")

    result = cursor.fetchall()

    return result


def get_AWS_CTRP_connection():
    """
    Use pg8000 to assign connection to UAT CTRP database on AWS Lambda (no SSH tunneling needed)
    :return:
    """
    database_info = Environment()
    logging.info("Instantiated environment variables")

    params = {
        'database': database_info.database_name,
        'user': database_info.database_user,
        'password': database_info.database_password,
        'host': database_info.database_host,
        'port': int(database_info.database_port)
    }

    try:
        conn = psycopg2.connect(**params)
        logging.info("Successfully connected")
        cursor = conn.cursor()
    except Exception as e:
        logging.error("Could not connect with pg8000")

    return cursor


import os


class Environment(object):
    def __init__(self):
        # self.database_name = os.environ['DATABASE_NAME']
        # self.database_ip = os.environ['DATABASE_IP']
        #
        # # self.ssh_port = os.environ['SSH_PORT']
        # # self.ssh_private_key = os.environ['SSH_PRIVATE_KEY']
        # # self.ssh_user = os.environ['SSH_USER']
        #
        # self.database_host = os.environ['DATABASE_HOST']
        # self.database_port = os.environ['DATABASE_PORT']
        # self.database_user = os.environ['DATABASE_USER']
        # self.database_password = os.environ['DATABASE_PASSWORD']
        #
        # self.local_host = os.environ['LOCAL_HOST']
        # self.local_port = os.environ['LOCAL_PORT']

        self.database_name = 'DATABASE_NAME'
        self.database_ip = 'DATABASE_IP'

        # self.ssh_port = os.environ['SSH_PORT']
        # self.ssh_private_key = os.environ['SSH_PRIVATE_KEY']
        # self.ssh_user = os.environ['SSH_USER']

        self.database_host = 'DATABASE_HOST'
        self.database_port = 10
        self.database_user = 'DATABASE_USER'
        self.database_password = 'DATABASE_PASSWORD'

        self.local_host = 'LOCAL_HOST'
        self.local_port = 'LOCAL_PORT'



class TestIntentClass(unittest.TestCase):

    @mock.patch("psycopg2.connect")
    def test_get_result_from_ctrp(self, mock_connect):
        query = ("SELECT COUNT (anatomic_site_name) FROM public.dw_study_anatomic_site WHERE anatomic_site_name = '{}'"
                .format('Leukemia'))
        expected = [['fake', 'row', 1], ['fake', 'row', 2]]

        mock_con = mock_connect.return_value  # result of psycopg2.connect(**connection_stuff)
        mock_cur = mock_con.cursor.return_value  # result of con.cursor(cursor_factory=DictCursor)
        mock_cur.fetchall.return_value = expected  # return this when calling cur.fetchall()

        result = get_result_from_ctrp(query)
        self.assertEqual(result, expected)