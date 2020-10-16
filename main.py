from additional_files.csvreader import read_csv_and_add_to_array
from manager.heap_sort import heap_sort
from manager.bubble_sort import bubble_sort
import timeit

#C:\Users\111\PycharmProjects\Algorithmisation(Lab1)\additional_files\Films.csv

if __name__ == '__main__':
    filename = input("Please write filename to copy data:")
    films_list = read_csv_and_add_to_array(filename)
    n= len(films_list)
    #Heapsort for duration_in_minutes: Ascending order
    print("Sorted with algorithm: HEAPSORT(ASCENDING ORDER)")
    start_time = timeit.default_timer()
    heap_sort(films_list)
    end_time = timeit.default_timer()
    print('Execution time: {} seconds'.format(end_time - start_time))
    for i in range (n):
        print(films_list[i])
    print("\n\n")
    print("Sorted with algorithm: BUBBLESORT(DESCENDING ORDER)")
    start_time = timeit.default_timer()
    bubble_sort(films_list)
    end_time = timeit.default_timer()
    print('Execution time: {} seconds'.format(end_time - start_time))
    for i in range(n):
        print(films_list[i])
    # print("Number of exchanges:")
    # print(bubble_sort_exchange_counter)
    # print("Number of comparisons:")
    # print(bubble_sort_comparison_counter)
