#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: 
 * Return: 0 on success
 */

int check_cycle(listint_t *list)
{
    listint_t *ptr = list;

    if (ptr == NULL)
        return (0);

    while (ptr)
    {
        if (ptr->next == list)
            return (1);
        ptr = ptr->next;
    }
    return (0);
}
