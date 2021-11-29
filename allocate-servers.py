#!/usr/bin/env python3

servers = []
duration = 1000

line = input()
while line != "end":
   start_time = int(line)

   # Search for a server which is available at time start_time.
   #
   i = 0
   while i < len(servers) and start_time < servers[i]:
      i += 1

   if i < len(servers):
      # Reallocate existing server i.
      #
      # It will next be free to accept new jobs at time
      # start_time + duration.
      servers[i] = start_time + duration
   else:
      # No available server found, allocate a new server.
      #
      # It will next be available to accept new jobs at time
      # start_time + duration.
      servers.append(start_time + duration)

   line = input()

print(len(servers))
