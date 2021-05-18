# petstore_api_testing

Code explanation

There are 4 methods implemented in the script which perform the following actions:
- get (available pets)
- post (adds new pet)
- put (updates pet status to sold)
- delete (deletes pet by ID)
There is one more method that gets and returns the status_code of get command.

At the end of the hw_api_test.py file, there's a menu used for method calls.
post_put_objects.py file contain 2 objects imported in main .py file.

Used Postman for execution of these calls before implementing them in python..

Execution instructions

1. In post_put_objects.py file, there are two objects defined, used as parameters for post and put commands. These must be modified in order to post or put the needed information.
2. Execute hw_api_test.py (Menu will appear)
3. Select the action needed to be performed.
4. To check availability, insert option (1) (The content of the returned json file is present in response.json)

After Post, Put, Delete methods are called, the availability could checked by running option (1) from the menu and manually search if the change took place.
Also, there are asserts implemented for each method to check if the commands ran successfully.

Real project

In a real project, I would treat the testing of this api more serious by addind many other  tests to check functionality, reliability, performance and security. 
Also, for each HTTP call, the response code and message should be checked.
