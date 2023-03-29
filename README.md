# spaceid-checker

#Space ID Domain Checker
This script allows you to check for available domains to buy on the Space ID platform. It uses the Space ID GraphQL API to retrieve a list of domains that match your search query and checks for domains that meet the following criteria:

Domain is not currently owned by anyone
Domain has an expiration date of 0
Domain is listed for sale at a price of 5 (in the native cryptocurrency of the network)
If a domain meets all of these criteria, the script prints its name and network (either .eth, .bnb, or .arb) along with its list price (if available).

Usage
Clone this repository to your local machine
Install the required packages by running pip install -r requirements.txt
Create a file named combinations.txt in the root directory of the repository, containing a list of domain name combinations to search for, one per line. For example:
Copy code
apple
banana
cherry
Run the script by running python domain_checker.py
Notes
This script requires a working internet connection to use the Space ID GraphQL API.
The script can take some time to run depending on the number of search queries in combinations.txt and the number of available domains that meet the search criteria.
The maximum number of threads that the script will use to execute queries concurrently is set to 1000. This value can be changed by modifying the max_threads variable in the domain_checker.py file.
License
This project is licensed under the MIT License - see the LICENSE file for details.
