heap_sort_exchange_counter = 0
heap_sort_comparison_counter = 0
def heap_sort(arr):
    global heap_sort_comparison_counter
    global heap_sort_exchange_counter
    heap_size= len(arr)
    build_max_heap(arr,heap_size)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] #swap
        heap_sort_exchange_counter=heap_sort_exchange_counter+1
        max_heapify(arr,i,0)
    print("Number of exchanges:")
    print(heap_sort_exchange_counter)
    print("Number of comparisons:")
    print(heap_sort_comparison_counter)

def find_left_child_pos(current_pos):
  return current_pos*2 + 1

def find_right_child_pos(current_pos):
  return current_pos*2 +2

def build_max_heap(arr, heap_size):
  for current_element_pos in range(heap_size//2 -1, -1 ,-1):
      max_heapify(arr, heap_size, current_element_pos)

def max_heapify(arr, heap_size, current_element_pos):
  global heap_sort_comparison_counter
  global heap_sort_exchange_counter
  left_child_pos= find_left_child_pos(current_element_pos)
  right_child_pos= find_right_child_pos(current_element_pos)
  largest_element_pos= current_element_pos
  if (left_child_pos < heap_size and arr[largest_element_pos].duration_in_minutes<arr[left_child_pos].duration_in_minutes):
      heap_sort_comparison_counter += 1
      largest_element_pos=left_child_pos
  if (right_child_pos < heap_size and arr[largest_element_pos].duration_in_minutes < arr[right_child_pos].duration_in_minutes):
      heap_sort_comparison_counter+=1
      largest_element_pos = right_child_pos
  if (largest_element_pos !=current_element_pos):
      heap_sort_comparison_counter+=1
      arr[current_element_pos], arr[largest_element_pos] = arr[largest_element_pos], arr[current_element_pos] #swap
      heap_sort_exchange_counter += 1
      max_heapify(arr, heap_size, largest_element_pos)


