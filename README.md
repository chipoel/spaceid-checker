<h1>spaceid-checker</h1>

<h2>Space ID Domain Checker</h2>

<p>This script allows you to check for available domains to buy on the Space ID platform. It uses the Space ID GraphQL API to retrieve a list of domains that match your search query and checks for domains that meet the following criteria:</p>

<ul>
  <li>Domain is not currently owned by anyone</li>
  <li>Domain has an expiration date of 0</li>
  <li>Domain is listed for sale at a price of 5 USD</li>
</ul>

<p>If a domain meets all of these criteria, the script prints its name and network (either .eth, .bnb, or .arb) along with its list price (if available).</p>

<h2>Usage</h2>

<ol>
  <li>Clone this repository to your local machine</li>
  <li>Install the required packages by running the following command in the project directory:</li>
  <pre>$ pip install -r requirements.txt</pre>
  <li>Create a file named <code>combinations.txt</code> in the root directory of the repository, containing a list of domain name combinations to search for, one per line. For example:</li>
  <pre>apple<br>banana<br>cherry</pre>
  <li>Run the script by running the following command in the project directory:</li>
  <pre>$ python run.py</pre>
</ol>

<h2>Notes</h2>

<ol>
  <li>This script requires a working internet connection to use the Space ID GraphQL API.</li>
  <li>The script can take some time to run depending on the number of search queries in <code>combinations.txt</code> and the number of available domains that meet the search criteria.</li>
  <li>The maximum number of threads that the script will use to execute queries concurrently is set to 1000. This value can be changed by modifying the <code>max_threads</code> variable in the <code>run.py</code> file.</li>
</ol>
