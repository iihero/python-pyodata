Advanced usage
==============

Batch requests
--------------

Example of batch request that contains 3 simple entity queries:

.. code-block:: python

    batch = northwind.create_batch()

    batch.add_request(northwind.entity_sets.Employees.get_entity(108))
    batch.add_request(northwind.entity_sets.Employees.get_entity(234))
    batch.add_request(northwind.entity_sets.Employees.get_entity(23))

    response = batch.execute()

    print(response[0].EmployeeID, response[0].LastName)
    print(response[1].EmployeeID, response[1].LastName)
    print(response[2].EmployeeID, response[2].LastName)


Example of batch request that contains simple entity query as well
as changest consisting of two requests for entity modification:

.. code-block:: python

    batch = northwind.create_batch()

    batch.add_request(northwind.entity_sets.Employees.get_entity(108))

    changeset = northwind.create_changeset()

    changeset.add_request(northwind.entity_sets.Employees.update_entity(45).set(LastName='Douglas'))

    batch.add_request(changeset)

    response = batch.execute()

    print(response[0].EmployeeID, response[0].LastName)


Error handling
--------------

PyOData returns *HttpError* when the response code does not match the expected
code. Basically the exception is raised for all status codes >= 400.

In the case you know the implementation of back-end part and you want to show
accurate errors reported by your service, you can replace *HttpError* by your
sub-class *HttpError* by assigning your type into the class member *VendorType* of
the class *HttpError*.

.. code-block:: python

    from pyodata.exceptions import HttpError

    class MyHttpError(HttpError):

        def __init__(self, message, response):
            super(MyHttpError, self).__init__('Better message', response)


    HttpError.VendorType = MyHttpError


The class *pyodata.vendor.SAP.BusinessGatewayError* is an example of such
an HTTP error handling.
