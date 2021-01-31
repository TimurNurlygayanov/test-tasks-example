# Write numbers from 1 to 10 in console. The solution should be inline
for i in {1..10}; do echo $i; done;

for i in `req 1 10`; do echo $i; done;

# Replace "test" to "TEST" in text file:
sed 's/test/TEST/g' test.txt > test.txt

# Print 3rd column and use : as a separator of the columns
cat test.txt | awk -F ':' '{ print $3 }'
date | awk '{print $2,$3,$6}'
# Print all lines which contain '0.0'
awk '/0.0/ {print}' test.txt

# Find str 'my_str' in all files in current dir
egrep -e 'my_str' -r ./

# Check number of free inodes on disks
df -hi

# check free RAM / SWAP
free -h

# Check who is using network port
sudo netstat -nlp | grep 80
# With new ss tool
sudo ss -ltnp | grep 80

# Check connections from the IP
sudo ss dst 62.228.174.87 -n

# Start web service on port 8080
nc -l -p 8080
# Connect to port 8080 on the other host
nc 10.88.88.140 8080
