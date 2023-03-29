# spaceid-checker

<h1>Space ID Domain Checker</h1>
This script allows you to check for available domains to buy on the Space ID platform. It uses the Space ID GraphQL API to retrieve a list of domains that match your search query and checks for domains that meet the following criteria:<br>
1. Domain is not currently owned by anyone<br>
2. Domain has an expiration date of 0<br>
3. Domain is listed for sale at a price of 5 (in the native cryptocurrency of the network)<br>
If a domain meets all of these criteria, the script prints its name and network (either .eth, .bnb, or .arb) along with its list price (if available).<br>

<h1>Usage</h1>
1. Clone this repository to your local machine<br>
2. Install the required packages by running ``pip install -r requirements.txt``<br>
3. Create a file named combinations.txt in the root directory of the repository, containing a list of domain name combinations to search for, one per line. For example:<br>
Copy code
`apple<br>
banana<br>
cherry`<br>
Run the script by running `python run.py`<br>
<h1>Notes</h1>
1. This script requires a working internet connection to use the Space ID GraphQL API.<br>
2. The script can take some time to run depending on the number of search queries in combinations.txt and the number of available domains that meet the search criteria.<br>
3. The maximum number of threads that the script will use to execute queries concurrently is set to 1000. This value can be changed by modifying the max_threads variable in the run.py file.
