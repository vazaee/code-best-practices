from normal_queue import NormalQueue
from priority_queue import PriorityQueue

# test_queue = NormalQueue()
# test_queue.update_queue()
# test_queue.update_queue()
# test_queue.update_queue()
# test_queue.update_queue()
# print(test_queue.call_customer(5))
# print(test_queue.call_customer(10))

test_queue_2 = PriorityQueue()
test_queue_2.update_queue()
test_queue_2.update_queue()
test_queue_2.update_queue()
print(test_queue_2.call_customer(10))
print(test_queue_2.call_customer(1))
print(test_queue_2.statistics('10/01/1993', 198, 'detail'))