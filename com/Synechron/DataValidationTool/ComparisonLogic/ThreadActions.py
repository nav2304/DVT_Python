from com.Synechron.DataValidationTool.ComparisonLogic.BalancedBinarySearchTree import BalancedTree
import threading

# Global Tree and root declaration
root = None
myTree = BalancedTree()


def operation_thread(lock, operation, key, values):
    lock.acquire()
    switcher = {
        'insert':insertSourceData(lock, key, values),
        'delete':deleteAndLogData(lock, key, values)
    }
    switcher.get(operation.lower())
    lock.release()


def insertSourceData(lock, key, value):
#     print('--------------------------------------------------------------------')
    global root, myTree
    root = myTree.insert(root, key)
#     print('--------------------------------------------------------------------')


def deleteAndLogData(lock, key, value):
    print('--------------------------------------------------------------------')
    global root, myTree
    root = myTree.preOrder(root)
    print('--------------------------------------------------------------------')


if __name__ == "__main__":
    lock = threading.Lock()
    switcher = {
        'insert':insertSourceData(lock, 1, ''),
        'delete':deleteAndLogData(lock, 1, '')
    }
    switcher.get('insert', lambda: "Invalid month")
#
#     for i in range(10):
# #         insertSourceData(i, '')
#         # setting global variable x as 0
#         # creating a lock
#         lock = threading.Lock()
#
#         # creating threads
#         t1 = threading.Thread(target=operation_thread, args=(lock, 'insert', i, ''))
#         t2 = threading.Thread(target=operation_thread, args=(lock, 'insert', i * 4, ''))
#         t3 = threading.Thread(target=operation_thread, args=(lock, 'delete', i * 4, ''))
#         # start threads
#         t1.start()
#         t2.start()
#         t3.start()
#         # wait until threads finish their job
#         t1.join()
#         t2.join()
#         t3.join()
#
# root = myTree.insert(root, 20)
# root = myTree.insert(root, 30)
# root = myTree.insert(root, 40)
# root = myTree.insert(root, 50)
# root = myTree.insert(root, 25)
# # root = myTree.insert(root, 35)
#
# """The constructed AVL Tree would be
#             30
#         / \
#         20 40
#         / \     \
#     10 25 50"""
#
# # Preorder Traversal
# print("Preorder traversal of the",
#       "constructed AVL tree is")
# myTree.preOrder(root)
# print()
#
# # This code is contributed by Ajitesh Pathak
