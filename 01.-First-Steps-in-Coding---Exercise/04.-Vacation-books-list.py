pages_in_current_book = int(input())
pages_per_hour = int(input())
days_to_be_read = int(input())

time_needed_to_read_the_book = pages_in_current_book // pages_per_hour
time_needed_per_day = time_needed_to_read_the_book / days_to_be_read

print (time_needed_per_day)