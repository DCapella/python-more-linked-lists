#########################
# !!! SOLUTION CODE !!! #
#########################


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        """
        Will remove any nodes with duplicated data.

        Parameters
        ----------
        head : obj
          A node that can contain a list of other nodes on method, next.

        Returns
        -------
        _ : None
          Does not return anything because it is printing instead.
        """
        # List to keep order
        results = []

        # While loop since we do not know how many heads.
        while True:
          # Check to see if it even has data and is unique.
          if head.data and head.data not in results:
            results.append(head.data)

          # Check to see if next, otherwise break.
          if head.next:
            head = head.next
          else:
            break

        # Print out unique results on one line.
        for i in results:
          print(i, end=" ")

mylist= Solution()
