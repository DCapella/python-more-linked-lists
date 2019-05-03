# Python More Linked Lists

#### [HackerRank](www.hackerrank.com)

> A Node class is provided for you in the editor.
> A Node object has an integer data field, data,
> and a Node instance pointer, next, pointing to
> another node (i.e.: the next node in a list).
> A removeDuplicates function is declared in your
> editor, which takes a pointer to the head node of a
> linked list as a parameter. Complete removeDuplicates
> so that it deletes any duplicate nodes from the list
> and returns the head of the updated list.
> Note: The head pointer may be null, indicating that the
> list is empty. Be sure to reset your next pointer when
> performing deletions to avoid breaking the list.

## Prework

![more-linked-lists](./more-linked-lists.png)

Pretty simple stuff especially after the previous problems.
The results will be a list in order to keep order (again, no pun intended).
I'll use a while loop since we do not know how many. Going to have to check
to make sure it even has data and that it is unique (not in) and finally if
it has a next. Once we break from the while loop, print each number on the
same line.

Here we go.

## Code

```python
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
```

## Conclusion
Even though this one was simple, it was still fun. Honestly, it was probably only a simple problem because of the previous problems.
