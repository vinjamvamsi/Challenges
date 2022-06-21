Problem statement:

We need to write code that will query the meta data of an instance within AWS and provide a
json formatted output. The choice of language and implementation is up to you.


Solution:

My approch is to query URL : http://169.254.169.254/latest/meta-data/ and parse the response to JSON format.
