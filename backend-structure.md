
* Resource->Module->Gateway


# Friends
* id
* sender
* receiver
* status
* date_sent
* data_accepted
* date_rejected

SELECT * FROM friends WHERE sender=userid
UNION 
SELECT * FROM friends WHERE receiver=userid
