book_pages = int(input())
pages_read_one_hour = int(input())
days_for_reading_the_book = int(input())

total_time_read = book_pages / pages_read_one_hour
hours_a_day = total_time_read / days_for_reading_the_book

print(int(hours_a_day))
