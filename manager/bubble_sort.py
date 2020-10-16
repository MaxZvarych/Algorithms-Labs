bubble_sort_exchange_counter = 0
bubble_sort_comparison_counter = 0
def bubble_sort(arr):
    global bubble_sort_comparison_counter
    global bubble_sort_exchange_counter
    for j in range(0, len(arr)-1, 1):
        for i in range(0, len(arr)-1-j, 1):
            if (arr[i].number_of_responces <arr[i+1].number_of_responces):
                bubble_sort_comparison_counter+=1
                arr[i], arr[i+1] = arr[i+1] , arr[i] #swap
                bubble_sort_exchange_counter+=1
    print("Number of exchanges:")
    print(bubble_sort_exchange_counter)
    print("Number of comparisons:")
    print(bubble_sort_comparison_counter)
