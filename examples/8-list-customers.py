# coding=utf-8
#
#  Example 8 - Retrieving all of your customers with offset and count
#
from __future__ import print_function

import sys, os

#
# Add Mollie library to module path so we can import it.
# This is not necessary if you use pip or easy_install.
#
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../'))

import Mollie


def main():
    try:
        #
        # Initialize the Mollie API library with your API key.
        #
        # See: https://www.mollie.com/dashboard/settings/profiles
        #
        mollie = Mollie.API.Client()
        mollie.setApiKey('test_bt7vvByF6jTcBR4dLuW66eNnHYNIJp')

        amount_of_customers_to_retrieve = 20

        #
        # Get the latest 20 customers
        #
        # See: https://www.mollie.com/nl/docs/reference/customers/list
        #
        customers = mollie.customers.all(offset=0, count=amount_of_customers_to_retrieve)

        body = '<p>Your API key has %u customers.</p>' % int(customers['totalCount'])

        if int(customers['totalCount']) == 0:
            return body

        if int(customers['totalCount']) > amount_of_customers_to_retrieve:
            body += '<p><b>Note: Only the first %s are shown here.</b></p>' % amount_of_customers_to_retrieve

        body += """
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Payment creation</th>
                        <th>Payment History</th>
                    </tr>
                </thead>
                <tbody>
        """

        for customer in customers:
            body += '<tr>'
            body += '<td>%s</td>' % customer['id']
            body += '<td>%s</td>' % customer['name']
            body += '<td>%s</td>' % customer['email']
            body += '<td><a href="/9-create-customer-payment?customer_id=%s">Create payment for customer</a></td>' % \
                    customer['id']
            body += '<td><a href="/10-customer-payment-history?customer_id=%s">Show payment history</a>' % \
                    customer['id']
            body += '</tr>'

        body += "</tbody></table>"

        return body

    except Mollie.API.Error as e:
        return 'API call failed: ' + e.message

if __name__ == '__main__':
    print(main())
